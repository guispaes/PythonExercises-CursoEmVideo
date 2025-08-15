def fatorial(numero, show=False):
    resultado = 1
    for c in range(numero, 1, -1):
        resultado *= c

    if show:
        for c in range(numero+1, 1, -1):
            if c > 2:
                print(f'{c - 1}', end=' x ')
            else:
                print(f'{c-1} = ', end='')

    return resultado

numero = int(input('Digite um número para calcular seu Fatorial: '))
while numero < 0:
    numero = int(input('O número deve ser inteiro e positivo.\nDigite um número para calcular seu Fatorial: '))
conta = str(input('Deseja ver a conta? [s/n] ').strip().upper())
while conta != 'S' and conta != 'N':
    conta = str(input('Deseja ver a conta? [s/n] ').strip().upper())
if conta == 'S':
    conta = bool(True)
else:
    conta = bool(False)

print(fatorial(numero, conta))


