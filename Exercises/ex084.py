Cadastro = []
Pessoas =  [], []
Contador = 0
while True:
    Cadastro.clear()
    Cadastro.append(str(input('Nome: ').title()))
    Cadastro.append(float(input('Peso: Kg')))
    Contador += 1
    if Contador == 1:
        Pessoas[0].append(Cadastro[:])
        Pessoas[1].append(Cadastro[:])
    elif Contador > 1 and Cadastro[1] > Pessoas[0][0][1]:
        Pessoas[0].clear()
        Pessoas[0].append(Cadastro[:])
    elif Contador > 1 and Cadastro[1] == Pessoas[0][0][1]:
        Pessoas[0].append((Cadastro[:]))
    elif Contador > 1 and Cadastro[1] < Pessoas[1][0][1]:
        Pessoas[1].clear()
        Pessoas[1].append(Cadastro[:])
    elif Contador > 1 and Cadastro[1] == Pessoas[1][0][1]:
        Pessoas[1].append((Cadastro[:]))

    Continuar = str(input('Quer continuar[S/N]? ')).upper()
    if Continuar != 'S' and Continuar != 'N':
        Continuar = str(input('Por favor, digite uma resposta válida. Quer continuar[S/N]? ')).upper()
    elif Continuar == 'N':
        break
    else:
        continue
print(f'Quantidade de pessoas cadastradas: {Contador}')
print(f'O peso mais pesado foi {Pessoas[0][0][1]}, e as pessoas que correspondem a esse peso são: ', end=' ')
for p in Pessoas[0]:
    print(p[0], end=' ')
print(f'\nO peso mais leve foi {Pessoas[1][0][1]}, e as pessoas que correspondem a esse peso são: ', end=' ')
for p in Pessoas[1]:
    print(p[0], end=' ')
