import re

with open('Exercicios Regex TXT/registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

cps = re.findall(r'Código Postal:\s*(\d{4}-\d{3})', conteudo)

print("Codigos postais extraidos do ficheiro")
for cp in cps:
    print(f"{cp}")