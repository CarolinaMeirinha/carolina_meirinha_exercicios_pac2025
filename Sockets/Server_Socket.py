# ==========================================
# SERVIDOR DE CHAT MULTIUTILIZADOR COM RGPD
# DETECAO DE DADOS PESSOAIS E ENGENHARIA SOCIAL
# ==========================================

import socket
import threading
import re
import logging
from datetime import datetime
import json
import sys
import os

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('chat_server.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

class ChatServer:
    def __init__(self, host='127.0.0.1', porta=12345):
        self.host = host
        self.porta = porta
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clientes = {}  # {socket: nome}
        self.dados_cliente = {}  # {nome: {dados_pessoais: [], tentativas_sociais: []}}
        self.lock = threading.Lock()
        
        # Padrões regex para deteção de dados pessoais
        self.padroes = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            
            # Telefone Portugal - aceita 2xx (fixo) e 9xx (movel)
            'telefone': r'\b(?:\+351|00351)?\s?[269][0-9]{8}\b',
            
            # IP (apenas IPv4)
            'ip': r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
            
            # Nome completo - restritivo
            'nome_completo': r'\b(?:[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]{2,})\s+(?:[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]{2,})(?:\s+(?:[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]{2,}))?\b',
            
            # Data nascimento (dd/mm/aaaa ou dd-mm-aaaa)
            'data_nascimento': r'\b(0[1-9]|[12][0-9]|3[01])[/-](0[1-9]|1[0-2])[/-](19|20)\d{2}\b',
            
            # Cartão crédito (4 grupos de 4 dígitos)
            'cartao_credito': r'\b(?:\d{4}[- ]?){3}\d{4}\b'
        }
        
        # Lista de palavras comuns que não devem ser detectadas como nome completo
        self.palavras_ignorar = [
            'ola', 'tudo', 'bem', 'como', 'esta', 'vai', 'sim', 'nao', 'ok', 'oi',
            'hi', 'hello', 'meu', 'numero', 'telefone', 'email', 'pega', 'ai', 'no',
            'esse', 'esse', 'aquele', 'este', 'isso', 'aquilo', 'qual', 'quem', 'quando',
            'onde', 'como', 'porque', 'para', 'com', 'sem', 'sobre', 'ate', 'de', 'em'
        ]
        
        # Criar diretório para dados
        os.makedirs('dados_utilizadores', exist_ok=True)
    
    def guardar_dados_cliente(self, nome_cliente, tipo_dado, valor_dado, mensagem):
        """Guarda dados pessoais associados ao cliente"""
        with self.lock:
            if nome_cliente not in self.dados_cliente:
                self.dados_cliente[nome_cliente] = {
                    'dados_pessoais': [],
                    'tentativas_engenharia_social': [],
                    'mensagens_bloqueadas': []
                }
            
            registo = {
                'tipo': tipo_dado,
                'valor': valor_dado,
                'mensagem_original': mensagem,
                'timestamp': datetime.now().isoformat()
            }
            
            self.dados_cliente[nome_cliente]['dados_pessoais'].append(registo)
            
            # Guardar em ficheiro individual por cliente
            ficheiro_cliente = f"dados_utilizadores/{nome_cliente}_dados.json"
            try:
                with open(ficheiro_cliente, 'a', encoding='utf-8') as f:
                    json.dump(registo, f, ensure_ascii=False)
                    f.write('\n')
                logging.info(f"Dados pessoais de {nome_cliente} guardados: {tipo_dado} -> {valor_dado}")
            except Exception as e:
                logging.error(f"Erro ao guardar dados de {nome_cliente}: {e}")
    
    def detecao_valida(self, tipo, valor, mensagem_completa):
        """Verifica se a deteção é válida (evita falsos positivos)"""
        
        # Para telefones - garantir que tem pelo menos 9 dígitos
        if tipo == 'telefone':
            digitos = re.sub(r'\D', '', valor)
            if len(digitos) in [9, 12]:
                if digitos.startswith('2') or digitos.startswith('9') or digitos.endswith('9'):
                    return True
            return False
        
        # Para nomes completos, verificar se parece um nome real
        if tipo == 'nome_completo':
            partes = valor.split()
            
            # Deve ter pelo menos 2 partes (nome e apelido)
            if len(partes) < 2:
                return False
            
            # Verificar cada parte
            for parte in partes:
                parte_lower = parte.lower()
                
                # Ignorar palavras comuns
                if parte_lower in self.palavras_ignorar:
                    return False
                
                # Ignorar se for muito curto (menos de 3 letras)
                if len(parte) < 3:
                    return False
                
                # Verificar se contém apenas letras (com acentos)
                if not re.match(r'^[A-Za-zÁÀÂÃÉÊÍÓÔÕÚÇáàâãéêíóôõúç]+$', parte):
                    return False
            
            # Verificar se o primeiro carácter de cada parte é maiúsculo
            for parte in partes:
                if not parte[0].isupper():
                    return False
            
            return True
        
        # Para IP - garantir formato válido
        if tipo == 'ip':
            partes = valor.split('.')
            if len(partes) != 4:
                return False
            for parte in partes:
                num = int(parte)
                if num < 0 or num > 255:
                    return False
            return True
        
        # Para emails - garantir formato válido
        if tipo == 'email':
            if '@' not in valor or '.' not in valor:
                return False
            return True
        
        # Para datas - garantir formato válido
        if tipo == 'data_nascimento':
            try:
                partes = re.split(r'[/-]', valor)
                if len(partes) != 3:
                    return False
                dia = int(partes[0])
                mes = int(partes[1])
                ano = int(partes[2])
                if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1900 or ano > 2026:
                    return False
                return True
            except:
                return False
        
        return True
    
    def detetar_dados_pessoais(self, mensagem, nome_cliente):
        """Deteta dados pessoais na mensagem e guarda"""
        dados_encontrados = []
        
        for tipo, padrao in self.padroes.items():
            matches = re.findall(padrao, mensagem, re.IGNORECASE)
            if matches:
                for valor in matches:
                    if isinstance(valor, tuple):
                        valor = '.'.join(valor)
                    
                    if self.detecao_valida(tipo, valor, mensagem):
                        dados_encontrados.append({
                            'tipo': tipo,
                            'dados': valor,
                            'cliente': nome_cliente,
                            'mensagem': mensagem,
                            'timestamp': datetime.now().isoformat()
                        })
                        self.guardar_dados_cliente(nome_cliente, tipo, valor, mensagem)
                        
                        logging.warning(f"DADOS PESSOAIS DETETADOS - {tipo}: {valor} - Cliente: {nome_cliente}")
                        
                        self.analisar_engenharia_social(mensagem, nome_cliente, tipo, valor)
                
        return dados_encontrados
    
    def analisar_engenharia_social(self, mensagem, nome_cliente, tipo_dado, valor):
        """Analisa e guarda padrões de engenharia social"""
        palavras_suspeitas = ['senha', 'password', 'credito', 'cartao', 'pin',
                             'conta bancaria', 'documento', 'cpf', 'rg', 'cc',
                             'codigo', 'validade', 'cvv', 'nif', 'contribuinte']
        
        mensagem_lower = mensagem.lower()
        
        for palavra in palavras_suspeitas:
            if palavra in mensagem_lower:
                tentativa = {
                    'cliente': nome_cliente,
                    'palavra_suspeita': palavra,
                    'tipo_dado': tipo_dado,
                    'dados_encontrados': valor,
                    'mensagem_completa': mensagem,
                    'timestamp': datetime.now().isoformat()
                }
                
                with self.lock:
                    if nome_cliente in self.dados_cliente:
                        self.dados_cliente[nome_cliente]['tentativas_engenharia_social'].append(tentativa)
                    else:
                        self.dados_cliente[nome_cliente] = {
                            'dados_pessoais': [],
                            'tentativas_engenharia_social': [tentativa],
                            'mensagens_bloqueadas': []
                        }
                
                ficheiro_se = f"dados_utilizadores/{nome_cliente}_engenharia_social.json"
                try:
                    with open(ficheiro_se, 'a', encoding='utf-8') as f:
                        json.dump(tentativa, f, ensure_ascii=False)
                        f.write('\n')
                except:
                    pass
                    
                logging.critical(f"ENGENHARIA SOCIAL DETETADA - Cliente: {nome_cliente} - Palavra: {palavra}")
                break
    
    def bloquear_mensagem(self, mensagem, nome_cliente, dados_encontrados):
        """Bloqueia mensagem com dados pessoais e guarda registo"""
        with self.lock:
            if nome_cliente in self.dados_cliente:
                self.dados_cliente[nome_cliente]['mensagens_bloqueadas'].append({
                    'mensagem': mensagem,
                    'dados_encontrados': dados_encontrados,
                    'timestamp': datetime.now().isoformat()
                })
        
        logging.info(f"Mensagem BLOQUEADA de {nome_cliente}: {mensagem}")
        tipos = list(set([d['tipo'] for d in dados_encontrados]))
        valores = [d['dados'] for d in dados_encontrados]
        alerta = f"[ALERTA RGPD] A sua mensagem foi BLOQUEADA! Contém dados pessoais: {', '.join(tipos)} -> {', '.join(valores)}"
        return alerta
    
    def enviar_para_todos(self, mensagem, socket_remetente=None, excluir_remetente=True):
        """Envia mensagem para todos os clientes"""
        with self.lock:
            for socket_cliente in self.clientes:
                if excluir_remetente and socket_cliente == socket_remetente:
                    continue
                try:
                    socket_cliente.send(mensagem.encode('utf-8'))
                except:
                    pass
    
    def enviar_para_um(self, mensagem, socket_destino):
        """Envia mensagem para um cliente específico"""
        try:
            socket_destino.send(mensagem.encode('utf-8'))
        except:
            pass
    
    def listar_clientes(self):
        """Retorna lista de clientes conectados"""
        with self.lock:
            return list(self.clientes.values())
    
    def tratar_cliente(self, socket_cliente, endereco):
        """Thread para tratar cada cliente"""
        nome_cliente = None
        
        try:
            socket_cliente.send("BEM-VINDO AO CHAT! Por favor, informe o seu nome: ".encode('utf-8'))
            nome_cliente = socket_cliente.recv(1024).decode('utf-8').strip()
            
            if not nome_cliente:
                socket_cliente.close()
                return
            
            with self.lock:
                self.clientes[socket_cliente] = nome_cliente
                self.dados_cliente[nome_cliente] = self.dados_cliente.get(nome_cliente, {
                    'dados_pessoais': [],
                    'tentativas_engenharia_social': [],
                    'mensagens_bloqueadas': []
                })
            
            logging.info(f"Cliente conectado: {nome_cliente} - {endereco}")
            
            self.enviar_para_todos(f"[SISTEMA] {nome_cliente} entrou no chat!", socket_cliente, excluir_remetente=False)
            
            lista_utilizadores = ", ".join(self.listar_clientes())
            socket_cliente.send(f"[SISTEMA] Conectado! Utilizadores online: {lista_utilizadores}\n".encode('utf-8'))
            socket_cliente.send("[COMANDOS] /msg <utilizador> <mensagem> - mensagem privada\n".encode('utf-8'))
            socket_cliente.send("[COMANDOS] /users - listar utilizadores online\n".encode('utf-8'))
            socket_cliente.send("[COMANDOS] /help - ajuda\n".encode('utf-8'))
            socket_cliente.send("[COMANDOS] exit - sair\n".encode('utf-8'))
            
            while True:
                try:
                    mensagem = socket_cliente.recv(1024).decode('utf-8')
                    
                    if not mensagem or mensagem.lower() == 'exit':
                        break
                    
                    if mensagem.startswith('/msg '):
                        partes = mensagem.split(' ', 2)
                        if len(partes) >= 3:
                            destino = partes[1]
                            msg_privada = partes[2]
                            
                            socket_destino = None
                            with self.lock:
                                for sock, nome in self.clientes.items():
                                    if nome.lower() == destino.lower():
                                        socket_destino = sock
                                        break
                            
                            if socket_destino:
                                dados_encontrados = self.detetar_dados_pessoais(msg_privada, nome_cliente)
                                
                                if dados_encontrados:
                                    alerta = self.bloquear_mensagem(msg_privada, nome_cliente, dados_encontrados)
                                    socket_cliente.send(f"\n{alerta}\n".encode('utf-8'))
                                else:
                                    self.enviar_para_um(f"[PRIVADO de {nome_cliente}]: {msg_privada}", socket_destino)
                                    socket_cliente.send(f"[SISTEMA] Mensagem privada enviada para {destino}\n".encode('utf-8'))
                                    logging.info(f"Mensagem privada de {nome_cliente} para {destino}: {msg_privada}")
                            else:
                                socket_cliente.send(f"[ERRO] Utilizador '{destino}' não encontrado\n".encode('utf-8'))
                        else:
                            socket_cliente.send("[ERRO] Uso: /msg <utilizador> <mensagem>\n".encode('utf-8'))
                    
                    elif mensagem.startswith('/users'):
                        utilizadores = self.listar_clientes()
                        socket_cliente.send(f"[SISTEMA] Utilizadores online: {', '.join(utilizadores)}\n".encode('utf-8'))
                    
                    elif mensagem.startswith('/help'):
                        ajuda = """
=== COMANDOS DISPONÍVEIS ===
/msg <utilizador> <mensagem> - Enviar mensagem privada
/users - Listar utilizadores online
/help - Mostrar esta ajuda
exit - Sair do chat

=== REGRAS RGPD ===
Não envie dados pessoais:
- Emails: exemplo@dominio.com
- Telefones: 912345678 ou 212345678 ou +351912345678
- IPs: 192.168.1.1
- Nomes completos: Ana Silva (começando com maiúscula, mínimo 3 letras)
- Datas de nascimento: 01/01/1990
- Cartões de crédito: 1234 5678 9012 3456

Mensagens com estes dados serão BLOQUEADAS!
===========================
"""
                        socket_cliente.send(ajuda.encode('utf-8'))
                    
                    else:
                        dados_encontrados = self.detetar_dados_pessoais(mensagem, nome_cliente)
                        
                        if dados_encontrados:
                            alerta = self.bloquear_mensagem(mensagem, nome_cliente, dados_encontrados)
                            socket_cliente.send(f"\n{alerta}\n".encode('utf-8'))
                            logging.info(f"Cliente {nome_cliente} teve mensagem bloqueada")
                        else:
                            mensagem_formatada = f"[{nome_cliente}]: {mensagem}"
                            self.enviar_para_todos(mensagem_formatada, socket_cliente, excluir_remetente=True)
                            socket_cliente.send("[SISTEMA] Mensagem enviada com sucesso!\n".encode('utf-8'))
                            logging.info(f"Mensagem de {nome_cliente}: {mensagem}")
                
                except Exception as e:
                    logging.error(f"Erro ao processar mensagem de {nome_cliente}: {e}")
                    break
                    
        except Exception as e:
            logging.error(f"Erro com cliente {endereco}: {e}")
        finally:
            with self.lock:
                if socket_cliente in self.clientes:
                    nome = self.clientes.pop(socket_cliente)
                    logging.info(f"Cliente desconectado: {nome}")
                    self.enviar_para_todos(f"[SISTEMA] {nome} saiu do chat!", socket_cliente, excluir_remetente=False)
            
            socket_cliente.close()
    
    def iniciar(self):
        """Inicia o servidor"""
        try:
            self.server_socket.bind((self.host, self.porta))
            self.server_socket.listen()
            logging.info(f"SERVIDOR INICIADO em {self.host}:{self.porta}")
            logging.info("Aguardando conexões...")
            logging.info("Modo: Servidor passivo - apenas gere mensagens")
            logging.info("Comandos disponíveis para clientes: /msg, /users, /help")
            
            while True:
                socket_cliente, endereco = self.server_socket.accept()
                thread = threading.Thread(target=self.tratar_cliente, args=(socket_cliente, endereco))
                thread.daemon = True
                thread.start()
                
        except KeyboardInterrupt:
            logging.info("Servidor encerrado pelo utilizador")
        except Exception as e:
            logging.error(f"Erro no servidor: {e}")
        finally:
            self.server_socket.close()
            logging.info("Servidor finalizado")

if __name__ == "__main__":
    servidor = ChatServer()
    servidor.iniciar()