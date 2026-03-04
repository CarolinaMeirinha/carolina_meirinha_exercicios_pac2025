# 6. Estado do servidor
status = input("Digite o status do servidor (ok/erro): ").strip().lower()
tempo = int(input("Digite o tempo de resposta (ms): "))

match status:
    case "ok" if tempo <= 200:
        print("Servidor ativo")
    case "ok" if tempo > 200:
        print("Servidor lento")
    case "erro":
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")