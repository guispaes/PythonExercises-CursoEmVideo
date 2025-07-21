Cadastro, PessoasLeves, PessoasPesadas = [], [], []
Contador = 0
while True:
    Cadastro.clear()
    Cadastro.append(str(input('Nome: ')))
    Cadastro.append(float(input('Peso: Kg')))
    Contador += 1
    if Contador == 1:
        PessoasLeves.append(Cadastro[:])
        PessoasPesadas.append(Cadastro[:])
    elif Contador > 1 and Cadastro[1] > PessoasPesadas[0][1]:
        PessoasPesadas.clear()
        PessoasPesadas.append(Cadastro[:])
    elif Contador > 1 and Cadastro[1] == PessoasPesadas[0][1]:
        PessoasPesadas.append((Cadastro[:]))
    elif Contador > 1 and Cadastro[1] < PessoasLeves[0][1]:
        PessoasLeves.clear()
        PessoasLeves.append(Cadastro[:])
    elif Contador > 1 and Cadastro[1] == PessoasLeves[0][1]:
        PessoasLeves.append((Cadastro[:]))

    Continuar = str(input('Quer continuar[S/N]? ')).upper()
    if Continuar != 'S' and Continuar != 'N':
        Continuar = str(input('Por favor, digite uma resposta válida. Quer continuar[S/N]? ')).upper()
    elif Continuar == 'N':
        break
    else:
        continue
print(f'Quantidade de pessoas cadastradas: {Contador}')
print(f'O peso mais pesado foi {PessoasPesadas[0][1]}, e as pessoas que correspondem a esse peso são: ', end=' ')
for p in PessoasPesadas:
    print(p[0], end=' ')
print(f'\nO peso mais leve foi {PessoasLeves[0][1]}, e as pessoas que correspondem a esse peso são: ', end=' ')
for p in PessoasLeves:
    print(p[0], end=' ')

