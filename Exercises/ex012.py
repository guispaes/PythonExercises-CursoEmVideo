print('Promoção de produto: ')
print(30*'=')
Preco = float(input('Qual o preço do produto? '))
print(30*'=')
Desconto = int(input('Quanto de desconto o produto receberá? '))
print(30*'=')
print(f'O produto custa R${Preco:.2f}\n'
      f'Com o desconto de {Desconto}%, custará: R${Preco-(Desconto/100*Preco):.2f}')
print(30*'=')
print('Fim do programa.')