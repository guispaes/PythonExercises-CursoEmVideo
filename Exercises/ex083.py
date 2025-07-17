Lista = []
ParentesesEsquerda = ParentesesDireita = 0
Expressao = str(input('Digite a expressão númerica: ').replace(' ', ''))

for palavra in Expressao:
    for letra in palavra:
        Lista.append(letra)

for c in range(len(Lista)):
    if Lista[c] == '(':
        ParentesesEsquerda += 1
    if Lista[c] == ')':
        ParentesesDireita += 1

if ParentesesDireita == ParentesesEsquerda:
    print('Sua expressão é correta!')
else:
    print('Sua expressão está incorreta!')