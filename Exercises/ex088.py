from time import sleep
from random import sample

JogosSorteados, JogoAtual = [], []
QuantidadeJogos = int(input('Quanto jogos serão gerados? '))
for c in range(0,QuantidadeJogos):
    JogoAtual.append(sample(range(1,61), 6))
    JogosSorteados.append(JogoAtual[:])
    JogoAtual.clear()
for c2 in range(0,QuantidadeJogos):
    print(f'Jogo {c2+1}: ', sorted(*JogosSorteados[c2]))
