Distancia = float(input('Qual a distância em quilômetros da viagem? '))
if Distancia <= 200:
    print(f'O valor da viagem é: R${Distancia*0.50:.2f}')
else:
    print(f'O valor da viagem é R${Distancia*0.45:.2f}')
