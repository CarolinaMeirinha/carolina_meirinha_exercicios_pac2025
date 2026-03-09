def ex16():
    pares = []
    while len(pares) < 30:
        num = int(input("Digite um numero par entre 1 e 50: "))
        if num >= 1 and num <= 50 and num % 2 == 0:
            pares.append(num)
        else:
            print("Invalido!")
    
    soma = 0
    for n in pares:
        soma = soma + n
    media = soma / 30
    print("Media: " + str(media))

ex16()