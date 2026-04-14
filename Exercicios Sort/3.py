palavra = "algoritmo"

def ordenar_caracteres(palavra):
    caracteres = list(palavra)
    for i in range(len(caracteres)):
        for j in range(i + 1, len(caracteres)):
            if caracteres[i] > caracteres[j]:
                caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
    return ''.join(caracteres)

print(ordenar_caracteres(palavra))