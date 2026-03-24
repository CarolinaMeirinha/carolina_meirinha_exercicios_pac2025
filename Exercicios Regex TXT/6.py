import re

with open('Exercicios Regex TXT/dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.pt\b'
emails_pt = re.findall(padrao, conteudo)

print("Emails com .pt")
for email in emails_pt:
    print(f"{email}")