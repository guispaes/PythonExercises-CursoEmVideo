Contagem = 0
Soma = 0
for Numero in range(0,501,3):
    if Numero % 2 == 1:
     Contagem = Contagem+1
     Soma += Numero
print(f'A soma de todos os {Contagem} e a soma entre eles é {Soma}')
