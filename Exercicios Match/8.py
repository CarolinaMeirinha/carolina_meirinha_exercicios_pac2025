# 8. Operação matemática
op = input("Digite a operação (soma/subtrai/multiplica/divide): ").strip().lower()
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

match op:
    case "soma":
        print(n1 + n2)
    case "subtrai":
        print(n1 - n2)
    case "multiplica":
        print(n1 * n2)
    case "divide":
        if n2 != 0:
            print(n1 / n2)
        else:
            print("Erro: divisão por zero")
    case _:
        print("Operação inválida")