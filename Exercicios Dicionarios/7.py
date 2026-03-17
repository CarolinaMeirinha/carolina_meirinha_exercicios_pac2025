d = {'a': 1, 'b': 2, 'c': 3}
d_invertido = {}

for chave, valor in d.items():
    d_invertido[valor] = chave

print(d_invertido)