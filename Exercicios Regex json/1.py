import json

with open('Exercicios Regex json/dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("Conteudo do ficheiro .json")
for pessoa in dados:
    print(f"Nome: {pessoa['nome']}")
    print(f"Email: {pessoa['email']}")
    print(f"NIF: {pessoa['nif']}")
    print(f"Telefone: {pessoa['telefone']}")
    print(f"Site: {pessoa['site']}")
    print("-" * 40)