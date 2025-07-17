Peso = float(input('Digite seu peso(Kg): '))
Altura = float(input('Digite sua altura(M): '))
IMC = Peso/Altura**2
if IMC < 18.5:
    print('Você está abaixo do peso ideal.')
elif IMC < 25:
    print('Você está no peso ideal.')
elif IMC < 30:
    print('Você está acima do peso.')
elif IMC < 40:
    print('Você está dentro de um quadro de obesidade.')
else:
    print('Você está dentro de um quadro de obesidade mórbida.')
