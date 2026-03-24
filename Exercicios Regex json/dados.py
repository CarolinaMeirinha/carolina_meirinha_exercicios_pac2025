import json
import re

dados_json = [
    {
        "nome": "Ana Costa",
        "email": "ana.costa@gmail.com",
        "nif": "123456789",
        "telefone": "912345678",
        "site": "https://www.anacosta.pt"
    },
    {
        "nome": "João Silva",
        "email": "joao_silva@empresa.com",
        "nif": "987654321",
        "telefone": "914-567-123",
        "site": "http://joaosilva.com"
    },
    {
        "nome": "Marta Dias",
        "email": "marta.dias@escola.edu",
        "nif": "192837465",
        "telefone": "210 987 654",
        "site": "https://marta.edu"
    }
]

with open('Exercicios Regex json/dados.json', 'w', encoding='utf-8') as fs:
    json.dump(dados_json, fs, indent=2, ensure_ascii=False)

print("✅ Ficheiro dados.json criado com sucesso!")

# Verificar o conteúdo criado
print("\n📄 Conteúdo do ficheiro:")
with open('Exercicios Regex json/dados.json', 'r', encoding='utf-8') as fs:
    conteudo = json.load(fs)
    print(json.dumps(conteudo, indent=2, ensure_ascii=False))