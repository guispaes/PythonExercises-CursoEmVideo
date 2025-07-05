Contagem = 0
SegundaContagem = 0
PrimeiroTermo = int(input('Primeiro termo: '))
Razao = int(input('Razão: '))

print(PrimeiroTermo, end=' -> ')
while Contagem != 10:
    PrimeiroTermo += Razao
    print(PrimeiroTermo, end=' -> ')
    Contagem += 1
print('Pausa')

SegundoTermo  = int(input('Quantos termos você quer mostrar a mais? '))

while SegundoTermo != 0:

    while SegundoTermo != SegundaContagem:
        PrimeiroTermo += Razao
        print(PrimeiroTermo, end=' -> ')
        SegundaContagem += 1
        Contagem += 1

    print('Pausa')
    SegundoTermo = int(input('\nQuantos termos você quer mostrar a mais? '))
    SegundaContagem = 0

print(f'Progressão finalizada com {Contagem} termos mostrados.')