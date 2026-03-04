# Exercício 7
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1*2 + n2*3 + n3*5) / 10

print(f"Média: {media:.1f}")
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")