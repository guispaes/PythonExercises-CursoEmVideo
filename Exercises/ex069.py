Contagem_18Anos = Contagem_Homens = Contagem_Mulheres_Menores = int(0)

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)

    #Atribui respostas as variáveis
    Idade = int(input('Idade: '))
    while 0 < Idade > 100:
        Idade = int(input('Por favor, digite uma idade maior que 0 e menor 100.\nIdade: '))

    Sexo = str(input('Sexo [M/F]: ').strip().upper())
    while Sexo != 'M' and Sexo != 'F':
        Sexo = str(input('Por favor, digite um sexo válido.\nSexo [M/F]: ').strip().upper())

    Continuar = str(input('Quer continuar? [S/N]: ').strip().upper())
    while Continuar != 'S' and Continuar != 'N':
        Continuar = str(input('Por favor, digite uma resposta válida.\nQuer continuar? [S/N]: ').strip().upper())

    if Idade >= 18: Contagem_18Anos += int(1)
    if Sexo == 'M': Contagem_Homens += int(1)
    if Idade < 20 and Sexo == 'F': Contagem_Mulheres_Menores += 1

    #Finaliza o loop.
    if Continuar == 'N':
        break

#Mostra os dados finais.

print(f'Total de pessoas com mais de 18 anos: {Contagem_18Anos}.\n'
      f'Total de homens cadastrados: {Contagem_Homens}.\n'
      f'Total de mulheres com menos de 20 anos cadastradas: {Contagem_Mulheres_Menores}.\n')
