import requests
import json
import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

USER_AGENT = "EducationalCrawler/1.0 (uso académico)"
DELAY = 1  # segundos entre pedidos

def obter_robots_parser(url_inicial):
    """Obtém e configura o parser do robots.txt"""
    parsed = urlparse(url_inicial)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = urljoin(base_url, "/robots.txt")
    
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except:
        print(f"[AVISO] Não foi possível ler {robots_url}")
    return rp

def pode_visitar(rp, url):
    """Verifica se o robots.txt permite visitar a URL"""
    return rp.can_fetch(USER_AGENT, url)

def extrair_dados(url, html):
    """Extrai título e links de uma página HTML"""
    soup = BeautifulSoup(html, "html.parser")
    
    # Título
    titulo = soup.find("title")
    titulo_texto = titulo.get_text().strip() if titulo else "Sem título"
    
    # Links
    links = []
    for link in soup.find_all("a", href=True):
        href_absoluto = urljoin(url, link["href"])
        links.append(href_absoluto)
    
    return {
        "url": url,
        "titulo": titulo_texto,
        "links": links
    }

def visitar_pagina(url):
    """Faz o pedido HTTP a uma página"""
    headers = {"User-Agent": USER_AGENT}
    
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f"[ERRO] {url} → Status: {resposta.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"[EXCEÇÃO] {url} → {e}")
        return None

def crawler(url_inicial, max_paginas):
    """
    Crawler ético que respeita robots.txt e não sobrecarrega servidores
    """
    # Obter robots.txt
    rp = obter_robots_parser(url_inicial)
    
    # Verificar se a página inicial é permitida
    if not pode_visitar(rp, url_inicial):
        print(f"[BLOQUEADO] robots.txt não permite visitar {url_inicial}")
        return []
    
    # Controlo de páginas
    visitadas = set()
    para_visitar = [url_inicial]
    resultados = []
    
    print(f"[INÍCIO] Crawler a partir de: {url_inicial}")
    print(f"[LIMITE] Máximo de páginas: {max_paginas}")
    
    while para_visitar and len(visitadas) < max_paginas:
        url_atual = para_visitar.pop(0)
        
        # Evitar repetições
        if url_atual in visitadas:
            continue
        
        # Verificar robots.txt para cada URL
        if not pode_visitar(rp, url_atual):
            print(f"[BLOQUEADO] {url_atual} (robots.txt)")
            visitadas.add(url_atual)
            continue
        
        print(f"[PROCESSAR] {url_atual}")
        
        # Obter o HTML da página
        html = visitar_pagina(url_atual)
        
        if html:
            # Extrair dados
            dados = extrair_dados(url_atual, html)
            resultados.append(dados)
            
            # Adicionar novos links à fila
            for link in dados["links"]:
                if link not in visitadas and link not in para_visitar:
                    para_visitar.append(link)
        
        # Marcar como visitada
        visitadas.add(url_atual)
        
        # Respeitar delay (boa prática)
        time.sleep(DELAY)
    
    print(f"[FIM] Crawler concluído. {len(resultados)} páginas guardadas.")
    return resultados

def guardar_json(dados, nome_ficheiro="resultados.json"):
    """Guarda os resultados em ficheiro JSON"""
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    print(f"[GUARDAR] Dados exportados para {nome_ficheiro}")

# ================= PROGRAMA PRINCIPAL =================
if __name__ == "__main__":
    # Configuração
    URL_INICIAL = "https://books.toscrape.com"
    MAX_PAGINAS = 5
    
    # Executar crawler
    dados_recolhidos = crawler(URL_INICIAL, MAX_PAGINAS)
    
    # Mostrar resumo
    print("\n" + "="*50)
    print("RESUMO:")
    print(f"Total de registos: {len(dados_recolhidos)}")
    
    for i, pagina in enumerate(dados_recolhidos, 1):
        print(f"  {i}. {pagina['titulo']} → {len(pagina['links'])} links")
    
    # Guardar resultados
    guardar_json(dados_recolhidos)