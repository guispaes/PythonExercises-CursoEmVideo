
Jogador = {"NomeJogador": str(input('Qual o nome do jogador? ').title()),
           "Partidas": int(input(f'Quantas partidas foram jogadas por ele? ')),
           "Gols": []}

for c in range(0, Jogador["Partidas"]):
    Jogador["Gols"].append(int(input(f'Gols feitos na partida {c+1}: ')))

print(f'\nO jogador {Jogador["NomeJogador"]} jogou {Jogador["Partidas"]} partidas.\n')
for c in range(0, Jogador["Partidas"]):
    print(f'Na partida {c+1}, fez {Jogador["Gols"][c]} gol(s).')
print(f'\nFez um total de {sum(Jogador["Gols"])} gol(s).')
