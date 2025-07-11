Total_Compra = Produto_Caro = Produto_Barato = Contador = 0
Nome_Produto_Barato = str('')

print('-'*30)
print('Carrinho de compras!')
print('-'*30)

while True:
        #Atribui respostas as variáveis
    Produto = str(input('Nome do produto: ').strip().title())
    Preco = float(input('Preço: R$').strip())
    Continuar = str(input('Quer continuar? [S/N]: ').strip().upper())
    Contador += 1
    while Continuar != 'S' and Continuar != 'N':
        Continuar = str(input('Por favor, digite uma resposta válida.\nQuer continuar? [S/N]: ').strip().upper())

    Total_Compra += Preco
    if 1000 <= Preco: Produto_Caro += 1
    if Contador == 1: Produto_Barato, Nome_Produto_Barato = Preco, Produto
    if  Preco < Produto_Barato: Produto_Barato, Nome_Produto_Barato = Preco, Produto

    #Finaliza o loop.
    if Continuar == 'N':
        break

#Mostra os dados finais.

print(f'O total da compra foi: R${Total_Compra:.2f}.\n'
      f'Quantidade de produtos que ultrapassam mil reais: {Produto_Caro}.\n'
      f'O produto mais barato foi a "{Nome_Produto_Barato}" e custou R${Produto_Barato:.2f}.\n')