from datetime import date

AnoAtual = date.today().year
AnoUsuario = int(input('Ano de nascimento: '))
if AnoAtual - AnoUsuario < 18:
    print(f'Quem nasceu em {AnoUsuario} tem {AnoAtual-AnoUsuario} anos em {AnoAtual}.\n'
          f'Ainda faltam {18-(AnoAtual-AnoUsuario)} para o alistamento.\n'
          f'Seu alistamento será feito em {AnoUsuario+18}.')
elif AnoAtual - AnoUsuario > 18:
    print(f'Quem nasceu em {AnoUsuario} tem {AnoAtual-AnoUsuario} anos em {AnoAtual}.\n'
          f'Você JÁ DEVERIA TER SE ALISTADO há {AnoAtual-AnoUsuario-18} anos\n'
          f'Seu alistamento foi feito em {AnoUsuario+18}.')
else:
    print(f'Quem nasceu em {AnoUsuario} completa 18 anos em {AnoAtual}.\n'
          f'Você deve se alistar imediatamente!!')
