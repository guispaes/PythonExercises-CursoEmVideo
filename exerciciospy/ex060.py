from math import factorial
'''Com while'''
Fatorial = int(input('Digite um número para calcular seu Fatorial: '))
Contagem = Fatorial-1
print(f'Calculando {Fatorial}!', end=f' = {Fatorial}')

while Contagem != 0:
    print(f' x {Contagem}', end='')
    Contagem -= 1

print(' =',factorial(Fatorial))

''' Com for'''
Fatorial = int(input('Digite um número para calcular seu Fatorial: '))
print(f'Calculando {Fatorial}!', end=f' = {Fatorial}')


for Contagem in range(Fatorial,1,-1):
    print(f' x {Contagem-1}', end='')
print(' =',factorial(Fatorial))
