Tupla =  ('Mouse', 78, 'Teclado', 299, 'Computador', 3550, 'Monitor', 1100)
for c in range(0,8,2):
    print(f'{Tupla[c]:-<20}R${Tupla[c+1]:>7.2f}')
