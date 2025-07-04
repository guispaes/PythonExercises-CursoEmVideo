PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razâo: '))

print(PrimeiroTermo, end=' -> ')
for Contagem in range(1,10):
    PrimeiroTermo += Razao
    print(PrimeiroTermo, end=' -> ')
print('Acabou')
