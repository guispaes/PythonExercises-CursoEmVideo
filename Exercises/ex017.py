from math import hypot
CatOposto = float(input('Comprimento do cateto oposto: '))
CatAdjacente = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(CatOposto, CatAdjacente):.2f}')
