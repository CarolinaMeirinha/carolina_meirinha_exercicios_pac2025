# 4. Tipo de dado
dado = eval(input("Digite um valor (ex: 10, 3.14, '123', 'texto', [1,2]): "))

match dado:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case str() if dado.isdigit():
        print("String numérica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Tipo desconhecido")