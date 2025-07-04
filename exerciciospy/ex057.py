RespostaUsuario = ''
while RespostaUsuario != 'M' and RespostaUsuario != 'F':
    RespostaUsuario = str(input('Informe seu sexo [M/F]: ').upper().strip())
    if RespostaUsuario != 'M' and RespostaUsuario != 'F':     
        print('Resposta Inválida.')
print('Ok!')
