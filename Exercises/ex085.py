Lista = [], [], []
for c in range(0,7):
    Lista[0].append(int(input(f'Digite o {c+1}° valor para ser adicionado a lista: ')))
    if Lista[0][c]%2==0:
        Lista[2].append(int(Lista[0][c]))
    else:
        Lista[1].append(int(Lista[0][c]))
print(f'Lista de pares: {sorted(Lista[2])}\n'
      f'Lista de impares: {sorted(Lista[1])}\n')
