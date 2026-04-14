palavras = ["banana", "uva", "abacaxi", "laranja"]

def ordenar_alfabetico(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:  # comparação direta (baseada em ASCII)
                lista[i], lista[j] = lista[j], lista[i]
    return lista

print(ordenar_alfabetico(palavras))