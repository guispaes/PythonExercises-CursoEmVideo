Segmento1 = float(input('Comprimento do primeiro segmento: '))
Segmento2 = float(input('Comprimento do segundo segmento: '))
Segmento3 = float(input('Comprimento do terceiro segmento: '))
if Segmento1+Segmento2>Segmento3 and Segmento1+Segmento3>Segmento2 and Segmento2+Segmento3>Segmento1:
    print('\Sim, é possível montar um triângulo com os segmentos informados.')
else:
    print('Não, é impossível montar um triângulo com as segmentos informados.')
