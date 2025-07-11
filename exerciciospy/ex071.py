Valor = int(input('Quanto você quer sacar? '))

Nota50 = Valor // 50
Nota20 = (Valor % 50) // 20
Nota10 = ((Valor % 50) % 20) // 10
Nota1 = (((Valor % 50) % 20) % 10) // 1

if Nota50 > 0:
    print(f'Total de {Nota50} cédulas de R$50')
if Nota20 > 0:
    print(f'Total de {Nota20} cédulas de R$20')
if Nota10 > 0:
    print(f'Total de {Nota10} cédulas de R$10')
if Nota1 > 0:
    print(f'Total de {Nota1} cédulas de R$1')
