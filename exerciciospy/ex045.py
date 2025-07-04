from random import choice
from time import sleep

ListaJogadas = [0, 1, 2]
JogadaCPU = choice(ListaJogadas)
JogadaUSER = int(input('Jogadas:'
                   '\n "0" para Pedra'
                   '\n "1" para Papel'
                   '\n "2" para Tesoura'
                   '\nEscolha sua jogada: '))
if JogadaUSER < 3:
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!\n')

    if JogadaUSER == 0 and JogadaCPU == 1:
        print(f'Usúario jogou Pedra\n'
              f'Computador jogou Papel\n\n'
              f'Computador Venceu!')
    elif JogadaUSER == 1 and JogadaCPU == 0:
        print(f'Usúario jogou Papel\n'
              f'Computador jogou Pedra\n\n'
              f'Usuário Venceu!')
    elif JogadaUSER == 1 and JogadaCPU == 2:
        print(f'Usúario jogou Papel\n'
              f'Computador jogou Tesoura\n\n'
              f'Computador Venceu!')
    elif JogadaUSER == 2 and JogadaCPU == 1:
        print(f'Usúario jogou Tesoura\n'
              f'Computador jogou Papel\n\n'
              f'Usuário Venceu!')
    elif JogadaUSER == 2 and JogadaCPU == 0:
        print(f'Usúario jogou Tesoura\n'
              f'Computador jogou Pedra\n\n'
              f'Computador Venceu!')
    elif JogadaUSER == 0 and JogadaCPU == 2:
        print(f'Usúario jogou Pedra\n'
              f'Computador jogou Tesoura\n\n'
              f'Usuário Venceu!')
    else:
        print('\nEMPATE!')
else:
    print('Jogada inválida')
