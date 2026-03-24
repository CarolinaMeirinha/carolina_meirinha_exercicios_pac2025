import json

with open('Exercicios Regex json/dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

with open('Exercicios Regex json/dados_nome_email.txt', 'w', encoding='utf-8') as f:
    f.write("NOME | EMAIL\n")
    
    for pessoa in dados:
        linha = f"{pessoa['nome']} | {pessoa['email']}\n"
        f.write(linha)

print("=== FICHEIRO CRIADO ===\n")
print("dados_nome_email.txt criado com sucesso!")
print("\nConteúdo do ficheiro:")

with open('Exercicios Regex json/dados_nome_email.txt', 'r', encoding='utf-8') as f:
    print(f.read())