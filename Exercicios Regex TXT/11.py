import re

with open('Exercicios Regex TXT/registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

nifs = re.findall(r'NIF:\s*(\d{9})', conteudo)
digitos_validos = ['1', '2', '3', '5', '6', '8']

print("Validar nifs do ficheiro")
for nif in nifs:
    if nif[0] in digitos_validos:
        print(f"{nif} - VÁLIDO (começa com {nif[0]})")
    else:
        print(f"{nif} - INVÁLIDO (começa com {nif[0]})")