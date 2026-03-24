import re

with open('Exercicios Regex TXT/registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

nifs = re.findall(r'NIF:\s*(\d{9})', conteudo)

print("Nifs extraidos do ficheiro")
for nif in nifs:
    print(f"{nif}")