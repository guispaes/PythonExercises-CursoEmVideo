Numero = int(input('Digite um número: '))
DivisorMedia = 1
MaiorNumero, MenorNumero = Numero, Numero
Media = float(Numero)
Continuar = str(input('Quer continuar? ').strip().upper())
while Continuar == 'S':
    Numero = int(input('Digite um número: '))
    Media += float(Numero)
    Continuar = str(input('Quer continuar? ').strip().upper())
    DivisorMedia += 1
    if  Numero > MaiorNumero:
        MaiorNumero = Numero
    elif Numero < MenorNumero:
        MenorNumero = Numero
print(f'Você digitou {DivisorMedia} números e a média foi {Media/DivisorMedia:.2f}\n'
      f'O maior número foi: {MaiorNumero}\n'
      f'Já o menor número foi: {MenorNumero}')
