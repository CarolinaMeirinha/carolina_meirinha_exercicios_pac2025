import re

with open ("Exercicios Regex TXT/dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

padrao = r'\b\d{9}\b|\b\d{3}-\d{3}-\d{3}\b|\b\d{3}\s\d{3}\s\d{3}\b'
telemoveis = re.findall(padrao, conteudo)

print("Estes sao todos os telemoveis do ficheiro: ")
for telemovel in telemoveis:
    print(telemovel)