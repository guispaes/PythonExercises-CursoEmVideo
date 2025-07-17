Lista= [(int(input('Digite cinco valores para ser adicionado a lista: ')))]

print(f'Adicionando o valor a ultima posição')

for c in range(0, 4):
    RespostaUsuario = (int(input('Digite cinco valores para ser adicionado a lista: ')))
    if c < 1:
        if  Lista[0] >  RespostaUsuario:
            Lista.insert(0, RespostaUsuario)
            print('Adicionando o número a posição 1...')
        elif Lista[len(Lista)-1] <= RespostaUsuario:
            Lista.insert(len(Lista), RespostaUsuario)
            print(f'Adicionando o valor a ultima posição')
    elif c < 2:
        if  Lista[0] >  RespostaUsuario:
            Lista.insert(0, RespostaUsuario)
            print('Adicionando o número a posição 1...')
        elif Lista [0] < RespostaUsuario < Lista[1]:
            Lista.insert(1, RespostaUsuario)
            print('Adicionando o número a posição 2...')
        elif Lista[len(Lista)-1] <= RespostaUsuario:
            Lista.insert(len(Lista), RespostaUsuario)
            print(f'Adicionando o valor a ultima posição')

    elif c < 3:
        if  Lista[0] >  RespostaUsuario:
            Lista.insert(0, RespostaUsuario)
            print('Adicionando o número a posição 1...')
        elif Lista [0] < RespostaUsuario < Lista[1]:
            Lista.insert(1, RespostaUsuario)
            print('Adicionando o número a posição 2...')
        elif Lista [1] < RespostaUsuario < Lista[2]:
            Lista.insert(1, RespostaUsuario)
            print('Adicionando o número a posição 3...')
        elif Lista[len(Lista)-1] <= RespostaUsuario:
            Lista.insert(len(Lista), RespostaUsuario)
            print(f'Adicionando o valor a ultima posição')

    elif c < 4:
        if  Lista[0] >  RespostaUsuario:
            Lista.insert(0, RespostaUsuario)
            print('Adicionando o número a posição 1...')
        elif Lista [0] < RespostaUsuario < Lista[1]:
            Lista.insert(1, RespostaUsuario)
            print('Adicionando o número a posição 2...')
        elif Lista [1] < RespostaUsuario < Lista[2]:
            Lista.insert(1, RespostaUsuario)
            print('Adicionando o número a posição 3...')
        elif Lista[3] < RespostaUsuario < Lista[4]:
            Lista.insert(1, RespostaUsuario)
            print('Adicionando o número a posição 4...')
        elif Lista[len(Lista)-1] <= RespostaUsuario:
            Lista.insert(len(Lista), RespostaUsuario)
            print(f'Adicionando o valor a ultima posição')

print(f'Você digitou os valores: ', end='')
print(*Lista, sep=", ")
