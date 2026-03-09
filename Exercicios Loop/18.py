def perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i
    if soma == n:
        return True
    else:
        return False

def ex18():
    limite = int(input("Digite um numero: "))
    for i in range(1, limite+1):
        if perfeito(i):
            print(i, end=" ")

ex18()