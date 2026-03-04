# 9. Processamento de requisição
metodo = input("Digite o método (GET/POST): ").strip().upper()
conteudo = input("Digite o conteúdo: ").strip()

match metodo:
    case "GET":
        print("Requisição GET recebida")
    case "POST" if conteudo != "":
        print("Requisição POST com dados válidos")
    case "POST":
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")