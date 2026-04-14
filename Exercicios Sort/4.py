palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contar_minusculas(palavra):
    return sum(1 for letra in palavra if 'a' <= letra <= 'z')

def ordenar_por_minusculas(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if contar_minusculas(lista[i]) > contar_minusculas(lista[j]):
                lista[i], lista[j] = lista[j], lista[i]
    return lista

print(ordenar_por_minusculas(palavras))