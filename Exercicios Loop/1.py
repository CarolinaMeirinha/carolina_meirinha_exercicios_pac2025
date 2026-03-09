def ex1():

    i = 0
    print("Numeros pares:")
    for i in range(1, 31):
        if i % 2 == 0:
            print(i, end=" ")

    print("\nNumeros impares:")
    for i in range(1, 31):
        if i % 2 != 0:
            print(i, end=" ")


ex1()