Ano = int(input('Digite um ano: '))
AnoStr = str(Ano)
if AnoStr.endswith('00'):
    if Ano%100 == 0 and Ano%400 == 0:
        print('O ano é bissexto')
    elif Ano%100 == 0 and Ano%400 != 0:
        print('O ano não é bissexto')
else:
    if Ano%4 == 00:
        print('O ano é bissexto')
    else:
        print('O ano não é bissexto')
