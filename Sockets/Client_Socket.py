# ==========================================
# CLIENTE DE CHAT MULTIUTILIZADOR COM RGPD
# ==========================================

import socket
import threading
import sys

class ChatClient:
    def __init__(self, host='127.0.0.1', porta=12345):
        self.host = host
        self.porta = porta
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nome = None
        self.conectado = False
        
    def receber_mensagens(self):
        """Thread para receber mensagens do servidor"""
        while self.conectado:
            try:
                mensagem = self.socket_cliente.recv(1024).decode('utf-8')
                if not mensagem:
                    break
                
                print(f"\n{mensagem}")
                print("\nVocê: ", end='', flush=True)
                
            except Exception as e:
                print(f"\n[ERRO] Conexão perdida: {e}")
                break
        
        self.conectado = False
        
    def iniciar(self):
        """Inicia o cliente"""
        try:
            self.socket_cliente.connect((self.host, self.porta))
            self.conectado = True
            
            solicitacao = self.socket_cliente.recv(1024).decode('utf-8')
            print(solicitacao)
            
            self.nome = input("Digite o seu nome: ")
            self.socket_cliente.send(self.nome.encode('utf-8'))
            
            print("\n[INFO] Conectado ao chat!")
            print("[COMANDOS]")
            print("   • exit - sair do chat")
            print("   • /msg <utilizador> <mensagem> - mensagem privada")
            print("   • /users - listar utilizadores online")
            print("   • /help - mostrar ajuda")
            print("\n" + "="*50)
            
            thread_receber = threading.Thread(target=self.receber_mensagens)
            thread_receber.daemon = True
            thread_receber.start()
            
            while self.conectado:
                try:
                    mensagem = input()
                    
                    if mensagem.lower() == 'exit':
                        print("[INFO] A encerrar conexão...")
                        self.socket_cliente.send("exit".encode('utf-8'))
                        break
                    elif mensagem.lower() == '/help':
                        self.socket_cliente.send("/help".encode('utf-8'))
                    elif mensagem.lower() == '/users':
                        self.socket_cliente.send("/users".encode('utf-8'))
                    elif mensagem.startswith('/msg '):
                        self.socket_cliente.send(mensagem.encode('utf-8'))
                    elif mensagem.strip():
                        self.socket_cliente.send(mensagem.encode('utf-8'))
                    
                except KeyboardInterrupt:
                    print("\n[INFO] A encerrar conexão...")
                    break
                except Exception as e:
                    print(f"[ERRO] {e}")
                    break
                    
        except ConnectionRefusedError:
            print("[ERRO] Não foi possível conectar ao servidor. Verifique se o servidor está em execução.")
        except Exception as e:
            print(f"[ERRO] {e}")
        finally:
            self.conectado = False
            self.socket_cliente.close()
            print("[INFO] Conexão encerrada.")

if __name__ == "__main__":
    cliente = ChatClient()
    cliente.iniciar()