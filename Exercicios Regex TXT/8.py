import re

with open('Exercicios Regex TXT/registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

datas = re.findall(r'Data:\s*(\d{2}/\d{2}/\d{4})', conteudo)

print("Datas extraidas do ficheiro")
for data in datas:
    print(f"{data}")