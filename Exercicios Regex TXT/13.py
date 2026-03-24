import re

from datetime import datetime

with open('Exercicios Regex TXT/registos.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

print("Registos anterios ao ano de 2025")

for linha in linhas:
    data_match = re.search(r'Data:\s*(\d{2})/(\d{2})/(\d{4})', linha)
    if data_match:
        dia, mes, ano = data_match.groups()
        data_registo = datetime(int(ano), int(mes), int(dia))
        data_limite = datetime(2025, 1, 1)
        
        if data_registo < data_limite:
            print(f"{data_registo.strftime('%d/%m/%Y')} - {linha.strip()}")