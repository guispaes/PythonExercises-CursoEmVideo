Numero = str(input('Informe um número de 0 a 9999: '))
NumeroStr = Numero.zfill(4)
print(f'Analisando o número "{Numero}", verificamos que:\n'
      f'Unidade: {NumeroStr[3]}\n'
      f'Dezena: {NumeroStr[2]}\n'
      f'Centena: {NumeroStr[1]}\n'
      f'Milhar: {NumeroStr[0]}\n')
