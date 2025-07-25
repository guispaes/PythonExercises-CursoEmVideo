from random import randint
from time import sleep

Jogadores = {'Jogador 1': randint(1,6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6)}
RankingJogadores, RankingPontuacao = [], []

print(f'Valores sorteados:\n')
for j, v in Jogadores.items():
    print(f'O {j} tirou {v}')
    sleep(1)
    RankingJogadores.append(j)
    RankingPontuacao.append(v)
print()

RankingJogadores.sort(reverse=True)
RankingPontuacao.sort(reverse=True)

print(F'{'RANKING FINAL':=^21}')
for c in range(0,4):
    print(f'{c+1}° lugar: {RankingJogadores[c]} - {RankingPontuacao[c]} pontos')
    sleep(1)
