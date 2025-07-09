Soma = Valor = Contador = 0

while True:
    Valor = int(input('Digite um valor (999 para parar): '))
    if Valor == 999: break
    Soma += Valor
    Contador += 1
print(f'A soma dos {Contador} valores foi {Soma}!')
