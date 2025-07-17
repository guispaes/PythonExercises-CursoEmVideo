Lista = [(int(input(f'Digite um valor para a Posição 0: ')))]
MenorNumero = MaiorNumero = Lista[0]

for c in range(1,5):
    Lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if Lista[c] < MenorNumero:
        MenorNumero = Lista[c]
    if Lista[c] > MaiorNumero:
        MaiorNumero = Lista[c]
print(f'Você digitou os valores: ', end='')
print(*Lista, sep=", ")
print(f'O maior valor digitado foi {MaiorNumero} nas posições', end=' ')
for c, n in enumerate(Lista, 0):
    if n == MaiorNumero:
        print(f'{c}', end=' ')
print(f'\nO menor valor digitado foi {MenorNumero} nas posições', end=' ')
for c, n in enumerate(Lista, 0):
    if n == MenorNumero:
        print(f'{c}', end=' ')
