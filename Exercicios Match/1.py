# 1. Tipo de dia
dia = input("Digite o nome de um dia da semana: ").strip().lower()

match dia:
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido")