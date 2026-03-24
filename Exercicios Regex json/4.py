import json
import re

with open('Exercicios Regex json/dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

padrao_nif = r'^[123568]\d{8}$'

print("Validação dos nifs")

for pessoa in dados:
    nif = pessoa['nif']
    if re.match(padrao_nif, nif):
        print(f"{pessoa['nome']}: {nif} - VÁLIDO")
    else:
        print(f"{pessoa['nome']}: {nif} - INVÁLIDO")