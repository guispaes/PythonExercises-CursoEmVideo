Soma = 0
Contagem = 0
Numero = int(input('Digite um número [999 para parar]: '))
while Numero != 999:
    Soma += Numero
    Contagem += 1
    Numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {Contagem} e a soma entre eles foi {Soma}')
