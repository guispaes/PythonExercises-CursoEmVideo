from random import choice
from time import sleep
print('Vou pensar em um número entre 1 e 5. Tente Adivinhar...')
Numero1 = 1
Numero2 = 2
Numero3 = 3
Numero4 = 4
Numero5 = 5
Resposta = choice([Numero1, Numero2, Numero3, Numero4, Numero5])
ChuteUsuario = int(input('Qual número eu pensei? '))
if ChuteUsuario < 1 or ChuteUsuario > 5:
    print('Por Favor, digite um número entre 1 e 5.')
else:
    if ChuteUsuario == Resposta:
        print('Processando...')
        sleep(2)
        print('Parabéns! Você venceu!')
    else:
        print('Processando...')
        sleep(2)
        print(f'Ganhei! Eu pensei no número {Resposta} e não no {ChuteUsuario}')
