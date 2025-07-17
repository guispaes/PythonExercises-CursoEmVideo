Numeros = int(input('Digite um número: '))
if Numeros % 2 == 1:
    Numeros = 0
for Contagem in range(1,6):
    OutroNumero = int(input('Digite outro: '))
    if OutroNumero % 2 == 0:
      Numeros = Numeros + OutroNumero
print(Numeros)
