# 5. Análise de mensagem
msg = input("Digite uma mensagem: ").strip().lower()

match msg:
    case "ola" | "bom dia":
        print("Saudação")
    case _ if msg.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in msg or "adeus" in msg:
        print("Despedida")
    case _:
        print("Mensagem genérica")