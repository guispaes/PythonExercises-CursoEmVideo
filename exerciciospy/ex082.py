Lista = [(int(input('Digite um valor para ser adicionado a lista: ')))]
ListaPar = []
ListaImpar = []
while True:
    RespostaUsuario = str(input('Quer continuar [S/N]? ').upper())
    if RespostaUsuario != 'S' and RespostaUsuario != 'N':
        RespostaUsuario = str(input('Por favor, digite uma opção válida.\n''Quer continuar [S/N]? ').upper())
    if RespostaUsuario == 'N':
        break
    Lista.append(int(input('Digite um  valor para ser adicionado a lista: ')))

for c in range(0,len(Lista)):
    if Lista[c]%2==0:
        ListaPar.append(int(Lista[c]))
    else:
        ListaImpar.append(int(Lista[c]))
print(f'Lista normal: {Lista}\n'
      f'Lista de pares: {ListaPar}\n'
      f'Lista de impares: {ListaImpar}\n')