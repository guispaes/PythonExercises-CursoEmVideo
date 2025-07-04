from random import randint
from time import sleep

print('Vou pensar em um número entre 0 e 10. Tente Adivinhar...')

Resposta = randint(0,10)
ChuteUsuario = int(-1)
Tentativas = int(0)
while Resposta != ChuteUsuario:
    ChuteUsuario = int(input('Qual número eu pensei? '))
    if ChuteUsuario < 0 or ChuteUsuario > 10:
        print('Por Favor, digite um número entre 0 e 10.')
    elif Resposta != ChuteUsuario:
        print('Processando...')
        sleep(1)
        print(f'Resposta errada!')
    Tentativas += 1
print('Processando...')
sleep(2)
print(f'Acertou com {Tentativas} tentativas. Eu pensei no {Resposta}! Você venceu!')
