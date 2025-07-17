NumeroUsuario = int(input('Digite um número inteiro: '))
RespostaUsuario = int(input('Escolha uma das bases para conversão:\n'
                            'Digite "1" para BINÁRIO\n'
                            'Digite "2" para OCTAL\n'
                            'Digite "3" para HEXADECIMAL\n\n'
                            'Sua opção: '))
if RespostaUsuario == 1:
    print(f'{NumeroUsuario} convertido para BINÁRIO é igual a \033[034m{bin(NumeroUsuario)[2:]}\033[m')
elif RespostaUsuario == 2:
    print(f'{NumeroUsuario} convertido para OCTAL é igual a \033[034m{oct(NumeroUsuario)[2:]}\033[m')
elif RespostaUsuario == 3:
    print(f'{NumeroUsuario} convertido para HEXADECIMAL é igual a \033[034m{hex(NumeroUsuario)[2:]}\033[m')
else:
    print('Você digitou uma resposta ínvalida.')
