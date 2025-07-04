Frase = str.lower(input('Digite uma frase: ').strip()).split()
FraseReferencia = ' '.join(Frase)
print(FraseReferencia.title())
print(f'A letra A aparece {FraseReferencia.count('a')} vezes\n'
      f'A primeira letra A apareceu na posição {FraseReferencia.find('a')+1}\n'
      f'A última letra A apareceu na posição {FraseReferencia.rfind('a')+1}')
