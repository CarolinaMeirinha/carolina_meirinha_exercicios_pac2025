import re

with open('Exercicios Regex TXT/dados.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

with open('Exercicios Regex TXT/extraidos.txt', 'w', encoding='utf-8') as f_out:
    print("A criar ficheiro extraidos")
    
    for linha in linhas:
        if linha.strip():  

            nome_match = re.search(r'Nome:\s*([^,]+)', linha)
            email_match = re.search(r'Email:\s*([^,\s]+)', linha)
            tel_match = re.search(r'Telemóvel:\s*([^\n]+)', linha)
            
            if nome_match and email_match and tel_match:
                nome = nome_match.group(1).strip()
                email = email_match.group(1).strip()
                telemovel = tel_match.group(1).strip()
                
                linha_nova = f"{nome} | {email} | {telemovel}\n"
                f_out.write(linha_nova)
                print(f"✅ {linha_nova.strip()}")

print("Ficheiro extraidos.txt criado com sucesso!")