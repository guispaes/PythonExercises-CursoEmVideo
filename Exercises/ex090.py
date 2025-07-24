Aluno = dict()

Aluno['Nome'] = str(input('Nome do Aluno: ').title()),

Aluno['Média'] = float(input(f'Média de {''.join(Aluno['Nome'])}: '))
if Aluno['Média']<0 or Aluno['Média'] > 10:
    Aluno['Média'] = float(input(f'Por favor, digite um valor entre 0 e 10.\n'
                                 f'Média de {''.join(Aluno['Nome'])}: '))
if Aluno['Média'] >= 6.0:
    Aluno['Status'] = 'Aprovado'
else:
    Aluno['Status'] = 'Reprovado'

print('='*20)
print(f"Aluno: {''.join(Aluno["Nome"])}\n"
      f"Média: {(Aluno['Média'])}\n"
      f"Status: {''.join(Aluno['Status'])}")
print('='*20)
