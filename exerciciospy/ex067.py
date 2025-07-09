Numero = int(input('Digite um número para ver sua tábuada: '))
while True:
    if Numero < 0: break
    print(20 * '-')
    for Multiplicador in range(0,11):
        print(f'{Numero:} x  {Multiplicador:2} = {Numero*Multiplicador}')
    print(20 * '-')
    Numero = int(input('\nDigite um número para ver sua tábuada: '))
print('Programa encerrado')
