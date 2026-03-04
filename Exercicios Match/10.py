# 10. Jogo: Pedra, Papel ou Tesoura
j1 = input("Jogador 1 (pedra/papel/tesoura): ").strip().lower()
j2 = input("Jogador 2 (pedra/papel/tesoura): ").strip().lower()

match (j1, j2):
    case (j1, j2) if j1 == j2:
        print("Empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")