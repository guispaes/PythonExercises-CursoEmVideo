Top20Brasileiro = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG', 'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo', 'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')

PosicaoTop20 = tuple(f'{Posicao}. {Time}' for Posicao, Time in enumerate(Top20Brasileiro, 1))
TimesOrdemAlfabetica = sorted(Top20Brasileiro)

print('Top 5 do Brasileirão:', *PosicaoTop20[:5], sep='\n')
print('\nZona de rebaixamento:', *PosicaoTop20[-4:], sep='\n')
print('\nTimes em ordem alfabética:', *TimesOrdemAlfabetica, sep='\n')
print(f'\nO Corinthians se encontra na posição {Top20Brasileiro.index('Corinthians')+1}° do Brasileirão')
