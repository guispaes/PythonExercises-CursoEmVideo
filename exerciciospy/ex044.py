ValorCompra = float(input('Valor da compra: R$'))
PagamentoCompra = int(input('Formas de pagamento:'
                            '\n[1] à vista no dinheiro'
                            '\n[2] à vista no cartão'
                            '\n[3] 2x no cartão'
                            '\n[4] 3x ou mais no cartão'
                            '\nDigite sua opção: '))
if PagamentoCompra == 1:
    Preco = ValorCompra-ValorCompra/100*10
    print('Pagamento à vista no dinheiro: 10% de desconto.'
          f'\nPreço a ser pago: R${Preco:.2f}')
elif PagamentoCompra == 2:
    Preco = ValorCompra-ValorCompra/100*5
    print('Pagamento à vista no cartão: 5% de desconto.'
          f'\nPreço a ser pago: R${Preco:2f}')
elif PagamentoCompra == 3:
    Preco = ValorCompra/2
    print('Pagamento 2x no cartão: Preço normal.'
          f'\nPreço a ser pago: 2x parcelas de R${Preco:2f}')
elif PagamentoCompra == 4:
    Parcela = int(input('Quantidade de parcelas: '))
    if Parcela >= 3:
        Preco = ValorCompra+ValorCompra/100*20
        print(f'Pagamento {Parcela}x no cartão: 20% de juros.'
              f'\nPreço a ser pago: {Parcela}x parcelas de R${Preco/Parcela:.2f}')
    else:
        print('Opção inválida.')
else:
    print('Opção inválida.')