Contagem = 0
PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))

print(PrimeiroTermo, end=' -> ')
while Contagem != 10:
    PrimeiroTermo += Razao
    print(PrimeiroTermo, end=' -> ')
    Contagem += 1
print('Acabou')
