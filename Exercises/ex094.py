Verificador = 0
MediaIdade = 0
ListaMulheres = []
Cadastro = [{"Nome": str(input('Nome: ').title()),
             "Sexo": str(input('Sexo: [M/F] ').upper()),
             "Idade": int(input('Idade: '))}]
while True:
    #Verifica o se o sexo é válido.
    while Cadastro[Verificador]["Sexo"] != 'M' and Cadastro[Verificador]["Sexo"] != 'F':
        Cadastro[Verificador]["Sexo"] = str(input('Por favor, digite uma opção válida.\n''Sexo: [M/F] ').upper())
    #Verifica status e atribui aos resultados finais.
    if Cadastro[Verificador]["Sexo"] == 'F':
        ListaMulheres.append([Cadastro[Verificador]["Nome"]].copy())
    MediaIdade += Cadastro[Verificador]["Idade"]
    #Verifica se o usuário deseja continuar
    RespostaUsuario = str(input('Quer continuar [S/N]? ').upper().strip())
    while RespostaUsuario != 'S' and RespostaUsuario != 'N':
        RespostaUsuario = str(input('Por favor, digite uma opção válida.\n''Quer continuar [S/N]? ').upper())
    if RespostaUsuario == 'N':
        break
    #repete o loop
    Verificador += 1
    print(MediaIdade)
    Cadastro.append({"Nome": str(input('Nome: ').title()),
                 "Sexo": str(input('Sexo: [M/F] ').upper()),
                 "Idade": int(input('Idade: '))})

#Resultados
print(f'O grupo tem {Verificador+1} pessoas.\n'
      f'A média de idade é de {MediaIdade/(Verificador+1):.1f}\n'
      f'As mulheres cadastradoras foram', *ListaMulheres, sep=', ')

print(f'Lista das pessoas que estão acima do valor médio de idade do grupo: ')
for c in range(0, len(Cadastro)):
    if Cadastro[c]["Idade"] > MediaIdade/(Verificador+1):
        print(Cadastro[c], sep=', ')

print('Fim do programa')
