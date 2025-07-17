from random import randint

VezesVencidas = 0
print('Vamos jogar par ou impar!')

while True:

    '''Atribui valores as variáveis:'''

    JogadaCPU = randint(1, 10)
    JogadaUsuario = int(input('Diga um valor entre 1 e 10: '))
    if 0<JogadaUsuario>10: JogadaUsuario = int(input('Diga um valor entre 1 e 10: '))
    ParImpar = str(input('Par ou Impar [P/I]? ').strip().upper())
    if ParImpar != 'P' and ParImpar != 'I':
        ParImpar = str(input('Par ou Impar [P/I]? ').strip().upper())
    Soma = JogadaCPU + JogadaUsuario
    if Soma%2==0:
        Resultado = 'PAR'
    else:
        Resultado = 'IMPAR'

    '''Mostra o resultado:'''

    if Resultado == 'PAR' and ParImpar == 'P' or Resultado == 'IMPAR' and ParImpar == 'I':
        VezesVencidas += 1
        print(f'\nVocê jogou {JogadaUsuario} e o computador {JogadaCPU}.\n'
              f'Total de {Soma}, {Resultado}!\n'
              'Você venceu!\n'
              'Vamos jogar novamente!\n')
    else:
        print(f'\nVocê jogou {JogadaUsuario} e o computador {JogadaCPU}.\n'
              f'Total de {Soma}, {Resultado}!\n'
              'Você perdeu!\n')
        break

'''Fim de jogo!'''

print(f'GAME OVER!\n'
      f'Você venceu {VezesVencidas} vez(es)!')
