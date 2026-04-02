# Sistema de Chat com Deteção de Dados Pessoais (RGPD)

## Descrição do Projeto

Este projeto foi desenvolvido no âmbito de um laboratório de programação em Python. Consiste num sistema de chat multutilizador com deteção automática de dados pessoais em conformidade com o RGPD, incluindo funcionalidades de prevenção de engenharia social.

O sistema permite que vários utilizadores se conectem a um servidor central e troquem mensagens em tempo real, quer em conversas públicas, quer em mensagens privadas. O servidor monitoriza todas as mensagens, bloqueia aquelas que contêm dados sensíveis e guarda registos das tentativas de violação de privacidade.

## Autores

- Carolina Meirinha

## Requisitos Técnicos

- Python 3.7 ou superior
- Não são necessárias bibliotecas externas (apenas módulos da biblioteca padrão)

## Estrutura do Projeto
Sockets/
├── Server_Socket.py                # Código do servidor
├── Client_Socket.py                # Código do cliente
├── chat_server.log                 # Registos do servidor (gerado automaticamente)
├── dados_utilizadores/             # Pasta com dados dos utilizadores
│ ├── [nome]_dados.json             # Dados pessoais de cada cliente
│ └── [nome]_engenharia_social.json # Tentativas de engenharia social
└── README.md # Este ficheiro


## Como Executar

### 1. Iniciar o Servidor

Vá até á pasta onde se localiza o seu codigo e clique na barra acima onde mostra o caminho ate ela, apague tudo e escreva cmd e dè enter.
Abra um terminal e execute:


python Server_Socket.py
O servidor ficará à escuta de conexões e mostrará mensagens de registo no terminal.

2. Iniciar os Clientes
Em terminais diferentes (um para cada utilizador), execute:


python Client_Socket.py
O cliente pedirá um nome de utilizador e depois estará pronto para enviar e receber mensagens.

Funcionalidades Implementadas:
Chat Multutilizador
O servidor aceita múltiplas conexões simultâneas usando threads

Cada cliente tem uma thread independente no servidor

O servidor mantém uma lista de todos os clientes conectados

Tipos de Mensagens:
Mensagens públicas: enviadas para todos os utilizadores no chat

Mensagens privadas: enviadas apenas para um utilizador específico (comando /msg)

Comandos Disponíveis no Cliente
Comando	Descrição
/msg <utilizador> <mensagem>	Envia mensagem privada
/users	Lista todos os utilizadores online
/help	Mostra ajuda com todos os comandos
exit	Sai do chat
Deteção de Dados Pessoais (RGPD)
O sistema deteta automaticamente os seguintes tipos de dados pessoais:

Tipo	            Exemplo	                                Padrão
Email	            exemplo@dominio.com	                    Qualquer formato de email válido
Telefone	        912345678, 212345678, +351912345678	    Números portugueses (2xx e 9xx)
IP	                192.168.1.1	                            Endereços IPv4
Nome completo	    Ana Silva, João Santos	                Nomes com maiúsculas e mínimo 3 letras
Data de nascimento	01/01/1990, 15-03-1995	                Formato dd/mm/aaaa ou dd-mm-aaaa
Cartão de crédito	1234 5678 9012 3456	                    16 dígitos agrupados de 4

Bloqueio de Mensagens:
Quando um cliente tenta enviar uma mensagem com dados pessoais, a mensagem é bloqueada

O cliente recebe um alerta informando que a mensagem foi bloqueada

A mensagem não é enviada para os outros utilizadores

O servidor regista a tentativa nos registos

Guardar Dados Associados ao Cliente:
Conforme solicitado no laboratório, o sistema guarda os dados pessoais associados a cada cliente:

Cada vez que um cliente tenta enviar dados pessoais, esses dados são guardados

Os dados são armazenados em ficheiros JSON individuais por cliente

São guardados na pasta dados_utilizadores/ com o formato [nome]_dados.json

Deteção de Engenharia Social:
O sistema monitoriza tentativas de engenharia social, detetando palavras suspeitas como:

senha, password, crédito, cartão, pin

conta bancária, documento, CC

código, validade, CVV, NIF

Quando detetadas, as tentativas são guardadas em dados_utilizadores/[nome]_engenharia_social.json.

Notificações do Sistema:
Quando um utilizador entra no chat, todos são notificados

Quando um utilizador sai, todos são notificados

Alertas de bloqueio são enviados apenas ao remetente

Registos:
O servidor mantém um ficheiro de registo (chat_server.log) com:

Conexões e desconexões de clientes

Deteção de dados pessoais

Mensagens bloqueadas

Tentativas de engenharia social

Erros do sistema

Testes Realizados:
Teste de Múltiplas Conexões
Foram testados 3 clientes simultâneos (carol, ana, joão), todos a comunicar em simultâneo sem problemas de desempenho.

Teste de Deteção de Dados Pessoais

Mensagem enviada	Resultado
exemplo@email.com	BLOQUEADO (email)
912345678	        BLOQUEADO (telefone)
212345678	        BLOQUEADO (telefone fixo)
192.168.1.1	        BLOQUEADO (IP)
Ana Silva	        BLOQUEADO (nome completo)
01/01/1990	        BLOQUEADO (data nascimento)
1234 5678 9012 3456	BLOQUEADO (cartão crédito)

Teste de Falsos Positivos

Mensagem enviada	Resultado
olá tudo bem	    NÃO bloqueia
o meu número	    NÃO bloqueia
telefone 123	    NÃO bloqueia

Teste de Mensagens Privadas

Comando	Resultado
/msg ana Olá, tudo bem?	Mensagem entregue apenas à ana
/msg carol Como estás?	Mensagem entregue apenas à carol
/msg utilizador_inexistente Olá	Erro: utilizador não encontrado

Teste de Engenharia Social

Mensagem enviada	            Resultado
Qual é a sua senha?	            Detetado e guardado
Dá-me o teu cartão de crédito	Detetado e guardado
Preciso do teu NIF	            Detetado e guardado

Exemplo de Execução
Terminal do Servidor
text
2026-04-01 11:50:59,577 - INFO - SERVIDOR INICIADO em 127.0.0.1:12345
2026-04-01 11:50:59,579 - INFO - Aguardando conexões...
2026-04-01 11:51:17,071 - INFO - Cliente conectado: carol - ('127.0.0.1', 53252)
2026-04-01 11:51:24,726 - INFO - Cliente conectado: ana - ('127.0.0.1', 63639)
2026-04-01 11:52:01,646 - WARNING - DADOS PESSOAIS DETETADOS - email: exemplo@email.com - Cliente: carol
2026-04-01 11:52:01,647 - INFO - Mensagem BLOQUEADA de carol
Terminal do Cliente
text
BEM-VINDO AO CHAT! Por favor, informe o seu nome:
Digite o seu nome: carol

[INFO] Conectado ao chat!
[COMANDOS]
   • exit - sair do chat
   • /msg <utilizador> <mensagem> - mensagem privada
   • /users - listar utilizadores online
   • /help - mostrar ajuda

==================================================
[SISTEMA] ana entrou no chat!

Você: olá ana
[ALERTA RGPD] A sua mensagem foi BLOQUEADA! Contém dados pessoais: nome_completo -> ana
Dados Guardados pelo Sistema
Ficheiro de registo (chat_server.log)
Regista todas as operações do servidor para auditoria.

Dados do cliente (dados_utilizadores/carol_dados.json)
json
{
  "tipo": "email",
  "valor": "exemplo@email.com",
  "mensagem_original": "o meu email é exemplo@email.com",
  "timestamp": "2026-04-01T11:52:01.645"
}
Tentativas de engenharia social (dados_utilizadores/carol_engenharia_social.json)
json
{
  "cliente": "carol",
  "palavra_suspeita": "senha",
  "tipo_dado": "email",
  "dados_encontrados": "exemplo@email.com",
  "mensagem_completa": "a minha senha é exemplo@email.com",
  "timestamp": "2026-04-01T11:52:23.114"
}
Limitações Conhecidas
As mensagens estão limitadas a 1024 bytes

O servidor não suporta reconexão automática após queda

Não há persistência do histórico de mensagens

Os nomes dos utilizadores devem ser únicos (não há validação)


## Conclusão

O sistema desenvolvido cumpre todos os requisitos do laboratório:

1. ✅ Servidor com socket e threading para múltiplos clientes
2. ✅ Cliente com interface CLI para envio e receção de mensagens
3. ✅ Deteção de 6 tipos de dados pessoais (RGPD)
4. ✅ Bloqueio de mensagens com dados sensíveis
5. ✅ Alertas RGPD para os clientes
6. ✅ Guardar dados pessoais associados a cada cliente
7. ✅ Deteção e registo de tentativas de engenharia social
8. ✅ Mensagens públicas e privadas
9. ✅ Notificações de entrada e saída de utilizadores
10. ✅ Comandos especiais (/msg, /users, /help, exit)
11. ✅ Registos de eventos no servidor
12. ✅ Persistência de dados em JSON

O código está disponível num repositório privado no GitHub, partilhado com o professor e com os elementos do grupo.

## Referências

- [RGPD - Regulamento Geral sobre a Proteção de Dados](https://gdpr-info.eu/)
- [Documentação do módulo socket do Python](https://docs.python.org/3/library/socket.html)
- [Expressões regulares em Python](https://docs.python.org/3/library/re.html)