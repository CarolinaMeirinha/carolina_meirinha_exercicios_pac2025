def ex9():
    num = int(input("Digite um numero: "))
    while num < 1 or num > 100:
        num = int(input("Invalido! Digite entre 1 e 100: "))
    print ("Numero Válido: " + str(num))

ex9()
