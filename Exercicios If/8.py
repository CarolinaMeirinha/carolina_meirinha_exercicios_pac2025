# Exercício 8
notas = []
soma = 0

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1} (0-20): "))
    notas.append(nota)
    soma += nota

media = soma / 10
acima_media = 0

for nota in notas:
    if nota >= media:
        acima_media += 1

print(f"Média: {media:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_media}")