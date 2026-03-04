# 7. Classificação de produto
categoria = input("Digite a categoria (eletrônico/alimento): ").strip().lower()
preco = float(input("Digite o preço: "))

match categoria:
    case "eletrônico" | "eletronico" if preco > 1000:
        print("Produto de luxo")
    case "eletrônico" | "eletronico":
        print("Produto comum")
    case "alimento":
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")