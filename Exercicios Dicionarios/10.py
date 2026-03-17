frase = input("Introduz uma frase: ")
palavras = frase.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)