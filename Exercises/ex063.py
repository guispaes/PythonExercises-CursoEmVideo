PrimeiroTermo = 0
SegundoTermo = 1
Soma = 0
Contagem = int(0)
QuantidadeTermos = int(input('SEQUÊNCIA DE FIBONACCI\n'
                          'Quantos termos você quer mostrar? '))

while Contagem < QuantidadeTermos:
    if Contagem < 1:
        print(PrimeiroTermo, end=' -> ')
        Contagem+=1
    elif Contagem < 3:
        print(SegundoTermo, end=' -> ')
        Contagem+=1
    elif Contagem < 4:
        Soma = PrimeiroTermo + (SegundoTermo+1)
        print(Soma, end=' -> ')
        PrimeiroTermo, SegundoTermo = Soma, Soma - 1
        Contagem += 1
    else:
        Soma = PrimeiroTermo + SegundoTermo
        print(Soma, end=' -> ')
        PrimeiroTermo, SegundoTermo = Soma, Soma-SegundoTermo
        Contagem += 1
print('Fim')
