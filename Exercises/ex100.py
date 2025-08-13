from random import randint

numeros = []

def sorteia():
    quantidade_de_sorteios = int(input('Quantos números serão sorteados? '))
    for c in range(0, quantidade_de_sorteios):
        numeros.append(randint(1,11))
    print(f'Números sorteados: {numeros}')

def soma_par():
    soma = 0
    for c in range(0,len(numeros)):
        if numeros[c]%2 == 0:
            soma += numeros[c]
    print(f'Somando os valores pares de {numeros}, chegamos ao resultado de: {soma}!')


sorteia()
soma_par()
