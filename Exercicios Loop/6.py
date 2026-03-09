def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ex6():
    primos = []
    num = 2
    while len(primos) < 10:
        if primo(num):
            primos.append(num)
        num = num + 1
    print(primos)

ex6()