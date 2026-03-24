import json
import re

with open('Exercicios Regex json/dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("=== VALIDAÇÃO DE EMAILS ===\n")

for pessoa in dados:
    email = pessoa['email']
    if re.match(padrao, email):
        print(f"{pessoa['nome']}: {email} - VÁLIDO")
    else:
        print(f"{pessoa['nome']}: {email} - INVÁLIDO")