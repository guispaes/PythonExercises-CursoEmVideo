MaiorPeso, MenorPeso = 0, 0
for Contagem in range(1,6):
    Resposta = float(input(f'Peso da {Contagem}a pessoa: '))
    if Resposta > MaiorPeso:
        MaiorPeso = Resposta
    else:
        MenorPeso = Resposta
if MaiorPeso == MenorPeso:
    print('Todos os pesos são iguais.')
else:
    print(f'O maior peso lido foi de {MaiorPeso}Kg\n'
          f'O menor peso lido foi de {MenorPeso}Kg')
