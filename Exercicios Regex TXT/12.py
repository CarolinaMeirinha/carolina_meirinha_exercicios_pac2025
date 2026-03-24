import re

with open('Exercicios Regex TXT/registos.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

with open('Exercicios Regex TXT/resumo.txt', 'w', encoding='utf-8') as f_out:
    print("Criar ficheiro resumo")
    
    for linha in linhas:
        nome = re.search(r'Nome:\s*([^|]+)', linha).group(1).strip()
        nif = re.search(r'NIF:\s*(\d{9})', linha).group(1)
        data = re.search(r'Data:\s*(\d{2}/\d{2}/\d{4})', linha).group(1)
        cp = re.search(r'Código Postal:\s*(\d{4}-\d{3})', linha).group(1)
        site = re.search(r'Site:\s*(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', linha).group(1)
        
        linha_resumo = f"{nome} | {nif} | {data} | {cp} | {site}\n"
        f_out.write(linha_resumo)
        print(f"{linha_resumo.strip()}")

print("Ficheiro resumo.txt criado!")