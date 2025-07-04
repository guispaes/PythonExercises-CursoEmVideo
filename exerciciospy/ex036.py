ValorImovel = float(input('Qual é o valor do imóvel? R$'))
ValorSalario = float(input('Qual é o valor do salário do comprador? R$'))
AnosFinanciamento = int(input('Em quantos anos será paga a casa? '))
ValorParcela = ValorImovel/(AnosFinanciamento*12)
if ValorParcela <= (ValorSalario/100*30):
    print('Financiamento aprovado!\n'
          f'O valor da parcela será equivalente a R${ValorParcela:.2f}.')
else:
    print('Financiamento negado!\n'
          f'O valor da parcela de R${ValorParcela:.2f} excede 30% do salário do pagador.')
