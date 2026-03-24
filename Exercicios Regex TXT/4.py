import re

with open ("Exercicios Regex TXT/dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

padrao = r'Nome:\s*([^,]+)'
nomes = re.findall(padrao, conteudo)

print("Estes sao todos os nomes do ficheiro: ")
for nome in nomes:
    print(nome)