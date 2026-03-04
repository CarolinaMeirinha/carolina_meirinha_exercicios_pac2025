# Exercício 4
saldo = float(input("Digite o saldo inicial: "))
cheque = float(input("Digite o valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo}")
else:
    print("Não é possível descontar o cheque. Saldo insuficiente.")