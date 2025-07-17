Numero = int(input('Digite um número: '))
Divisao = int(0)
for Contagem in range(1, Numero+1):
    if Numero % Contagem == 0:
        print(f'\033[32m{Contagem}\033[m', end=' ')
        Divisao += 1
    else:
        print(f'\033[34m{Contagem}\033[m', end=' ')
if Divisao == 1:
        print(f'\nO número foi divido {Divisao} vez\n'
              f'E por isso, ele É PRIMO!')
elif Divisao <= 2:
    print(f'\nO número foi divido {Divisao} vezes\n'
          f'E por isso, ele É PRIMO!')
else:
    print(f'\nO número foi divido {Divisao} vezes\n'
          f'E por isso, ele NÃO É PRIMO!')