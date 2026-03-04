# Exercício 5
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort()

print(f"Crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
print(f"Decrescente: {numeros[2]}, {numeros[1]}, {numeros[0]}")