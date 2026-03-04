# 3. Tipo de pedido
tipo = input("Digite o tipo (compra/venda): ").strip().lower()
valor = float(input("Digite o valor: "))

match tipo:
    case "compra":
        print(f"Compra de {valor}€")
    case "venda":
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido")