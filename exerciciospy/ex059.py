PrimeiroValor = int(input('Primeiro Valor: '))
SegundoValor = int(input('Segundo Valor: '))

print('\n'
      '[1] Somar os valores digitados.\n'
      '[2] Multiplicar os valores digitados.\n'
      '[3] Maior valor entre os números.\n'
      '[4] Digitar outros valores.\n'
      '[5] Sair do programa.\n')

RespostaUsuario = int(input('Qual é sua opção? '))

while RespostaUsuario != 5:

    if RespostaUsuario == 1:
        print(f'\n{PrimeiroValor} + {SegundoValor} = {PrimeiroValor+SegundoValor}')
    elif RespostaUsuario == 2:
        print(f'\n{PrimeiroValor} x {SegundoValor} = {PrimeiroValor*SegundoValor}')
    elif RespostaUsuario == 3:
        if PrimeiroValor > SegundoValor:
            print(f'\n{PrimeiroValor} > {SegundoValor}')
        elif SegundoValor > PrimeiroValor:
            print(f'\n{SegundoValor} > {PrimeiroValor}')
        else:
            print('\nOs valores são iguais.')
    elif RespostaUsuario == 4:
        PrimeiroValor = int(input('\nPrimeiro Valor: '))
        SegundoValor = int(input('Segundo Valor: '))
    else:
        print('\nDigite uma resposta válida.')

    print('\n'
          '[1] Somar os valores digitados.\n'
          '[2] Multiplicar os valores digitados.\n'
          '[3] Maior valor entre os números.\n'
          '[4] Digitar outros valores.\n'
          '[5] Sair do programa.')

    RespostaUsuario = int(input('\nQual é sua opção? '))

print('\nPrograma finalizado.')
