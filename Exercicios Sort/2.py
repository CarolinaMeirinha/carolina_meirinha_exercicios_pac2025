palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

def ordenar_inverso_ignore_case(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            # comparar minúsculas, mas ordem inversa
            if lista[i].lower() < lista[j].lower():
                lista[i], lista[j] = lista[j], lista[i]
    return lista

print(ordenar_inverso_ignore_case(palavras))