NomeCompleto = str.title(input('Digite seu nome completo: '))
print(f'Muito prazer, {NomeCompleto[:(NomeCompleto.find(' '))]}{NomeCompleto[(NomeCompleto.rfind(' ')):]}!')
