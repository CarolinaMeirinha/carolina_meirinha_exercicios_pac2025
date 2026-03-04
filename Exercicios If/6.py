# Exercício 6
nome = input("Digite o nome do cliente: ")
compra = float(input("Digite o valor da compra: "))

if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

total = compra - desconto

print(f"Nome: {nome}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {total:.2f}€")