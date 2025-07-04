PrimeiroNumero = int(input('Digite um número: '))
SegundoNumero = int(input('Digite outro: '))
if PrimeiroNumero > SegundoNumero:
    print('O\033[34m primeiro\033[m número é\033[34m maior!\033[m')
elif PrimeiroNumero < SegundoNumero:
    print('O\033[34m segundo\033[m número é \033[34m maior!\033[m')
else:
    print('Os números são\033[34m iguais!\033[m')