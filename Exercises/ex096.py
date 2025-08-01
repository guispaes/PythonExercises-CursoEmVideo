def area(largura, comprimento):
    area = largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')


print('Controle de Terrenos:')
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
