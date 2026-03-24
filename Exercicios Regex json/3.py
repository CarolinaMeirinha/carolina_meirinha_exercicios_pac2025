import json
import re

with open('Exercicios Regex json/dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Padrão para extrair domínios
padrao = r'(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

print("Dominios dos sites")

for pessoa in dados:
    site = pessoa['site']
    dominio_match = re.search(padrao, site)
    if dominio_match:
        dominio = dominio_match.group(1)
        print(f"{pessoa['nome']}: {dominio}")