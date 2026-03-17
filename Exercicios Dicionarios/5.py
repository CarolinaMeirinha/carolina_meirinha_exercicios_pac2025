palavra = input("Introduz uma palavra: ")
contagem = {}

for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)