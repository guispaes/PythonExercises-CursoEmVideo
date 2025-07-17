Salario = float(input('Qual o salário do(a) colaborador(a)? '))
print('-'*30)
if Salario > 1250:
    print(f'O antigo salário do(a) colaborador(a) era R${Salario:.2f}\n'
          f'Com o um aumento de 10%, passa a receber: R${Salario+(Salario/100*10):.2f}')
else:
    print(f'O antigo salário do(a) colaborador(a) era R${Salario:.2f}\n'
          f'Com o novo aumento de 15%, passa a receber: R${Salario+(Salario/100*15):.2f}')
