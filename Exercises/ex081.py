Lista = [(int(input('Digite um valor para ser adicionado a lista: ')))]
c = 0

while True:
    c += 1
    RespostaUsuario = str(input('Quer continuar [S/N]? ').upper())
    if RespostaUsuario != 'S' and RespostaUsuario != 'N':
        RespostaUsuario = str(input('Por favor, digite uma opção válida.\n''Quer continuar [S/N]? ').upper())
    if RespostaUsuario == 'N':
        break
    Lista.append(int(input('Digite um  valor para ser adicionado a lista: ')))
if 5 in Lista:
    Cinco = 'Sim!'
else:
    Cinco = 'Não!'
print(f'{c} números foram digitados.\n'
      f'Lista em ordem decrescente: {', '.join(map(str, sorted(Lista, reverse=True)))}\n'
      f'O valor 5 foi digitado? {Cinco}')