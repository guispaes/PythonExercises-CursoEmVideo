from datetime import date
from itertools import count

ListaMaiores, ListaMenores = [], []

for Contagem in range(1,11):
    Resposta = int(input(f'Em que ano a {Contagem}a pessoa nasceu? '))
    if  date.today().year - Resposta < 18:
        ListaMenores.append(Resposta)
    else:
        ListaMaiores.append(Resposta)
print(f'{len(ListaMaiores)} pessoas são maiores de idade\n'
      f'{len(ListaMenores)} pessoas são menores de idade' )
