def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ex4():
    num = int(input("Digite um numero: "))
    if primo(num):
        print("Primo")
    else:
        print("Nao primo")

ex4()