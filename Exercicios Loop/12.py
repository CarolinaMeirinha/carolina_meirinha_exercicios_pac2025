def ex12():
    num = int(input("Digite um numero: "))
    cont = 0
    
    for i in range(1, num):
        print(str(num) + " + " + str(i) + " = " + str(num+i))
        print(str(num) + " - " + str(i) + " = " + str(num-i))
        print(str(num) + " * " + str(i) + " = " + str(num*i))
        if i != 0:
            print(str(num) + " / " + str(i) + " = " + str(num/i))
        cont = cont + 4
    
    print("Operacoes: " + str(cont))

ex12()