print('Reajuste salárial: \n'+30*'=')
Salario = float(input('Qual o salário do funcionário? R$'))
print(30*'=')
Aumento = int(input('Quanto de aumento receberá? %'))
print(30*'='+
      f'\nEste funcionário recebe R${Salario:.2f}\n'
      f'Com um aumento de {Aumento}%, receberá: R${Salario+(Aumento/100*Salario):.2f}\n'
      +30*'=')
