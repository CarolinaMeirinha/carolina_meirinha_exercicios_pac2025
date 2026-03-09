def ex3():

    i = 0
    soma = 0
    for i in range(10):
        nota = float(input("Digite a nota: "))
        soma = soma + nota
    media = soma / 10
    print("Media: " + str(media))


ex3()
