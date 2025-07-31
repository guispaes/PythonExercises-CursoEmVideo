Jogadores = []
#Cadastro de jogadores
while True:
    Jogador = {"NomeJogador": str(input('Qual o nome do jogador? ').title()),
               "Partidas": int(input(f'Quantas partidas foram jogadas por ele? ')),
               "Gols": []}

    for c in range(0, Jogador["Partidas"]):
        Jogador["Gols"].append(int(input(f'Gols feitos na partida {c+1}: ')))
    Jogadores.append(Jogador.copy())

    RespostaUsuario = str(input('Quer continuar [S/N]? ').upper().strip())
    while RespostaUsuario != 'S' and RespostaUsuario != 'N':
        RespostaUsuario = str(input('Por favor, digite uma opção válida.\n''Quer continuar [S/N]? ').upper())
    if RespostaUsuario == 'N':
        break
#Planilha de jogadores
print(f'{"N°":<5}{"Nome":<30}{"Gols":<40}Total')
print(80 * "-")
for c in range(len(Jogadores)):
    nome = Jogadores[c]["NomeJogador"]
    gols = str(Jogadores[c]["Gols"])
    total = sum(Jogadores[c]["Gols"])
    print(f'{c:<5}{nome:<30}{gols:<40}{total}')
print(80 * "-")

#Mostrar dados segundo índice
while True:
    Indice = int(input(f'\n{'MOSTRAR DADOS DO JOGADOR':^50}\n'
                      f'{'Utilize o índice a esquerda para a seleção':^50}\n'
                      f'{'Utilize o índice n°999 para interromper o programa':^50}\n'
                      f'? '))

    while Indice > len(Jogadores)-1:
        Indice = int(input('Por favor, digite uma resposta válida.\n '
                          '? '))
    if Indice == 999:
        break
    print(f'\nLevantamento do jogador {Jogadores[Indice]["NomeJogador"]}!\n')
    for c in range(0, Jogadores[Indice]["Partidas"]):
        print(f'Na partida {c + 1}, fez {Jogadores[Indice]["Gols"][c]} gol(s).')
