Palavra = str(input('Digite uma frase: ').upper().replace(' ', ''))
Palindromo = (''.join(reversed(Palavra)))
if Palavra == Palindromo:
    print('É palindromo')
else:
    print('Nem')
