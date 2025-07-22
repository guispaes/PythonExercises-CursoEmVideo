Matriz = [], [], []
NumerosPares = 0
MaiorValorSegundaLinha = 0

for m1 in range(0,3):
    Matriz[0].append(int(input(f'Digite um valor para [0,{m1}]: ')))
    if Matriz[0][m1]%2==0:
        NumerosPares += Matriz[0][m1]
for m2 in range(0,3):
    Matriz[1].append(int(input(f'Digite um valor para [1,{m2}]: ')))
    if Matriz[1][m2]%2==0:
        NumerosPares += Matriz[1][m2]
    if m2 == 0:
        MaiorValorSegundaLinha = Matriz[1][0]
    elif m2 > 0:
        if Matriz[1][m2] > MaiorValorSegundaLinha:
            MaiorValorSegundaLinha = Matriz[1][m2]
for m3 in range(0,3):
    Matriz[2].append(int(input(f'Digite um valor para [2,{m3}]: ')))
    if Matriz[2][m3]%2==0:
        NumerosPares += Matriz[2][m3]

print(f'[{Matriz[0][0]}] [{Matriz[0][1]}] [{Matriz[0][2]}]\n'
      f'[{Matriz[1][0]}] [{Matriz[1][1]}] [{Matriz[1][2]}]\n'
      f'[{Matriz[2][0]}] [{Matriz[2][1]}] [{Matriz[2][2]}]\n')

print(f'A soma dos valores pares é {NumerosPares}')
print(f'A soma dos valores da terceira coluna é {Matriz[0][2]+Matriz[1][2]+Matriz[2][2]}')
print(f'O maior valor da segunda linha é {MaiorValorSegundaLinha}')
