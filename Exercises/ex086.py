Matriz = [], [], []
for m1 in range(0,3):
    Matriz[0].append(int(input(f'Digite um valor para [0,{m1}]: ')))
for m2 in range(0,3):
    Matriz[1].append(int(input(f'Digite um valor para [1,{m2}]: ')))
for m3 in range(0,3):
    Matriz[2].append(int(input(f'Digite um valor para [2,{m3}]: ')))

print(f'[{Matriz[0][0]}] [{Matriz[0][1]}] [{Matriz[0][2]}]\n'
      f'[{Matriz[1][0]}] [{Matriz[1][1]}] [{Matriz[1][2]}]\n'
      f'[{Matriz[2][0]}] [{Matriz[2][1]}] [{Matriz[2][2]}]\n')
