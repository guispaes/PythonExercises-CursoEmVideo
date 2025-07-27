from datetime import datetime

AnoAtual = datetime.today().year
Cadastro = {"Nome": str(input('Nome: ')),
            "Ano": int(input('Ano de Nascimento: ')),
            "CTPS": int(input('Carteira de trabalho: '))}

if Cadastro["CTPS"] == 0:

    print(f'Nome: {Cadastro["Nome"]}\n'
          f'Idade: {AnoAtual - (Cadastro["Ano"])}\n'
          f'CTPS: O usuário não possui carteira de trabalho.')

else:

    Cadastro["Contratação"] = int(input('Primeiro ano de contratação: '))
    Cadastro["Salário"] = float(input('Salário: '))

    print(f'Nome: {Cadastro["Nome"]}\n'
          f'Idade: {AnoAtual - (Cadastro["Ano"])}\n'
          f'CTPS: {Cadastro["CTPS"]}\n'
          f'Primeira contratação: {Cadastro["Contratação"]}\n'
          f'Salário: R${Cadastro["Salário"]:.2f}\n\n'
          f'{Cadastro["Nome"]} irá se aposentar com {(Cadastro["Contratação"] - Cadastro["Ano"]) + 35} anos.')
