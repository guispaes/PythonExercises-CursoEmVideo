Valor1 = int(input('Primeiro valor: '))
Valor2 = int(input('Segundo valor: '))
Valor3 = int(input('Terceiro valor: '))
if Valor1 > Valor2 and Valor1 > Valor3:
    MaiorValor = Valor1
elif Valor2 > Valor1 and Valor2 > Valor3:
    MaiorValor = Valor2
else:
    MaiorValor = Valor3
print(f'O maior valor digitado foi {MaiorValor}')
if Valor1 < Valor2 and Valor1 < Valor3:
    MenorValor = Valor1
elif Valor2 < Valor1 and Valor2 < Valor3:
    MenorValor = Valor2
else:
    MenorValor = Valor3
print(f'O menor valor digitado foi {MenorValor}')
