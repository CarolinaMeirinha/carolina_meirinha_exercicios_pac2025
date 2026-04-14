palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

def agrupar_e_ordenar(lista):
    grupos = {}
    for palavra in lista:
        letra_inicial = palavra[0]
        if letra_inicial not in grupos:
            grupos[letra_inicial] = []
        grupos[letra_inicial].append(palavra)

    # ordenar cada grupo
    for letra in grupos:
        grupo = grupos[letra]
        for i in range(len(grupo)):
            for j in range(i + 1, len(grupo)):
                if grupo[i] > grupo[j]:
                    grupo[i], grupo[j] = grupo[j], grupo[i]

    return grupos

print(agrupar_e_ordenar(palavras))