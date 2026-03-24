import json
import re

with open('Exercicios Regex json/dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def validar_nif(nif):
    padrao = r'^[123568]\d{8}$'
    return re.match(padrao, nif) is not None

def validar_telefone(telefone):
    telefone_limpo = re.sub(r'[-\s]', '', telefone)
    return re.match(r'^\d{9}$', telefone_limpo) is not None

registos_validos = []

print("Registos que sao validos")

for pessoa in dados:
    email_valido = validar_email(pessoa['email'])
    nif_valido = validar_nif(pessoa['nif'])
    telefone_valido = validar_telefone(pessoa['telefone'])
    
    print(f"{pessoa['nome']}:")
    print(f"  Email: {'✅' if email_valido else '❌'} {pessoa['email']}")
    print(f"  NIF: {'✅' if nif_valido else '❌'} {pessoa['nif']}")
    print(f"  Telefone: {'✅' if telefone_valido else '❌'} {pessoa['telefone']}")
    
    if email_valido and nif_valido and telefone_valido:
        registos_validos.append(pessoa)
        print(f"REGISTO VÁLIDO - Será guardado\n")
    else:
        print(f"REGISTO INVÁLIDO - Não será guardado\n")

# Guardar registos válidos
with open('Exercicios Regex json/registos_validos.json', 'w', encoding='utf-8') as f:
    json.dump(registos_validos, f, indent=2, ensure_ascii=False)

print(f"\nFicheiro 'registos_validos.json' criado com {len(registos_validos)} registos válidos!")