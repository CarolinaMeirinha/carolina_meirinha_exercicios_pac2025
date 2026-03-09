def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def contar_divisores(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1
    return cont

def perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i
    if soma == n:
        return True
    return False

def teste1():
    print("1 - Analisar numeros")
    print("2 - Calculadora")
    print("3 - Tabuada")
    print("4 - Sair")
    op = input("Escolha: ")
    
    if op == "1":
        n = int(input("Digite um numero (1-30000): "))
        if n >= 1 and n <= 30000:
            for i in range(n, 0, -1):
                print("\nNumero: " + str(i))
                if primo(i):
                    print("Primo: Sim")
                else:
                    print("Primo: Nao")
                print("Divisores: " + str(contar_divisores(i)))
                if perfeito(i):
                    print("Perfeito: Sim")
                else:
                    print("Perfeito: Nao")
                
                if i % 10 == 1 and i != n:
                    r = input("Continuar? (s/n): ")
                    if r != "s":
                        break
        else:
            print("Invalido")
    
    elif op == "2":
        n1 = float(input("Numero 1: "))
        n2 = float(input("Numero 2: "))
        opc = input("Operacao (+, -, *, /): ")
        if opc == "+":
            print(n1 + n2)
        elif opc == "-":
            print(n1 - n2)
        elif opc == "*":
            print(n1 * n2)
        elif opc == "/":
            if n2 != 0:
                print(n1 / n2)
            else:
                print("Erro")
        else:
            print("Invalido")
    
    elif op == "3":
        maximo = int(input("Maximo (1-1000): "))
        if maximo >= 1 and maximo <= 1000:
            for num in range(1, maximo+1):
                print("\nTabuada do " + str(num))
                for i in range(1, 11):
                    print(str(num) + " x " + str(i) + " = " + str(num*i))
                if num % 20 == 0 and num != maximo:
                    r = input("Continuar? (s/n): ")
                    if r != "s":
                        break
        else:
            print("Invalido")
    
    elif op == "4":
        print("Adeus")

teste1()