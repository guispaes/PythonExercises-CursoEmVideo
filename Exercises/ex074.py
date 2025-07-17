from random import randint
#Gera os números dentro da tupla
NumerosGerados = tuple(randint(0,100) for c in range(0,5))
print('Os números gerados foram: ', end='')
print(*NumerosGerados, sep=' - ')
#Transforma o item 0 da tupla como menor e maior número
MaiorNumeroGerado = MenorNumeroGerado = int(NumerosGerados[0])
#Confere se os outros itens são maiores ou menos que o primeiro item
for c in range(0,5):
    if int(NumerosGerados[c]) < MenorNumeroGerado:
       MenorNumeroGerado = int(NumerosGerados[c])
for c in range(0,5):
    if int(NumerosGerados[c]) > MaiorNumeroGerado:
        MaiorNumeroGerado = (NumerosGerados[c])
#Retorna o resultado
print(f'Maior número: {MaiorNumeroGerado}\n'
      f'Menor número: {MenorNumeroGerado}')