import re

# Exercício 10: Extrair domínios dos sites
with open('Exercicios Regex TXT/registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

# Padrão para domínios (www.exemplo.pt, empresa.com, escola.edu)
dominios = re.findall(r'(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', conteudo)

print("Dominios extraidos do ficheiro")
for dominio in dominios:
    print(f"{dominio}")