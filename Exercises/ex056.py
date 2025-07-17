#Categoriza variáveis
ListaNome, ListaIdade, ListaSexo = [], [], []
MaiorIdadeMasculina, NomeMaiorIdadeMasculina = 0,''
QuantidadeMulher = 0

#Recebe as respostas do usúario e as salva nas variáveis.
for Contagem in range(0,4):
    print(f'{Contagem+1}a PESSOA')
    ListaNome.append(str(input('Nome: ')))
    ListaIdade.append(int(input('Idade: ')))
    ListaSexo.append(str(input('Sexo [M/F]: ').upper().strip()))
    if ListaSexo[Contagem] == 'M':
        if ListaIdade[Contagem] > MaiorIdadeMasculina:
          MaiorIdadeMasculina = ListaIdade[Contagem]
          NomeMaiorIdadeMasculina = ListaNome[Contagem]
    if ListaSexo[Contagem] == 'F' and ListaIdade[Contagem] < 20:
        QuantidadeMulher = QuantidadeMulher+1

#Mostra as variáveis na tela.
print(f'A média da idade do grupo é de {sum(ListaIdade)/len(ListaIdade)} anos')
print(f'O homem mais velho tem {MaiorIdadeMasculina} anos e se chama {NomeMaiorIdadeMasculina}\n'
      f'{QuantidadeMulher} mulheres tem menos de 20 anos.')
