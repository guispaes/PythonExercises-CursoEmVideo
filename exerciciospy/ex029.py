Velocidade = int(input('Qual a velocidade do carro? '))
if Velocidade > 80:
    Multa = float(Velocidade-80)*7
    print('Você foi multado por excesso de velocidade\n'
          f'O valor a ser pago é equivalente a: R${Multa:.2f}')
else:
    print('O veículo está dentro do limite de velocidade, continue dirigindo com segurança.')
