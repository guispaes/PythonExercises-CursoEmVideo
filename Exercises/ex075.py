Tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite um último número: ')))

print('Você digitou os valores: ', end='')
print(*Tupla, sep=', ')


#Verifica a quantidades de valores '9' na tupla
QuantidadeIgualNove = 0
for c in range(0,4):
    if int(Tupla[c]) == 9: QuantidadeIgualNove += 1
print(f'O valor "9" apareceu {QuantidadeIgualNove} vezes')


# Verifica onde o valor '3' foi digitado na tupla
PrimeiroValorTres = 0
for c in range(0,4):
    if int(Tupla[c]) == 3:
        PrimeiroValorTres = c
        break
if PrimeiroValorTres:
    print(f'O primeiro valor "3" apareceu na posição {PrimeiroValorTres+1}')
else:
    print('O valor "3" não digitado em nenhuma posição!')


#Verifica os valores pares
AlgumPar = 0
for c in range(0,4):
    if int(Tupla[c]) % 2 == 0:
        AlgumPar += 1
if AlgumPar:
    print('Os números pares que foram digitados são: ', end=' ')
    for c in range(0,4):
        if int(Tupla[c]) % 2 == 0:
            if c < 3:
                print(int(Tupla[c]), end=', ')
            else:
                print(int(Tupla[c]))
if AlgumPar == 0: print('Nenhum número par foi digitado!')
