import re as reg

with open ("Exercicios Regex TXT/dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

padrao= r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = reg.findall(padrao,conteudo)

print("Todos os emails do ficheiro: ")
for email in emails: 
    print (email)