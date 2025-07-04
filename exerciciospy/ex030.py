Resposta = int(input('Digite um número: '))
Numero = str(Resposta)
if Numero.endswith('0') or Numero.endswith('2') or Numero.endswith('4') or Numero.endswith('6') or Numero.endswith('8'):
    print(f'{Numero} é um número par.')
else:
    print(f'{Numero} é um número impar.')
