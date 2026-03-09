def contardivisor(n):
    cont = 0
    for i in range(1, n+1):
        if n % 1 == 0:
            cont = cont + 1
    return cont

def ex10():
    num = int(input("Digite um numero: "))
    print("Divisores: " + str(contardivisor(num)))


ex10()