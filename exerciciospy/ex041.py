from datetime import date

AnoNascimento = int(input('Ano de Nascimento: '))
Idade = date.today().year - AnoNascimento
print(f'Quem nasceu em {AnoNascimento} tem {Idade} anos.')
if Idade <= 9:
    print('Atleta: Mirim')
elif Idade <= 14:
    print('Atleta : Infantil')
elif Idade <= 19:
    print('Atleta: Junior')
elif Idade <= 25:
    print('Atleta: Sênior')
else:
    print('Atleta: Master')
