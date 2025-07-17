Lista = [(int(input('Digite cinco valores para ser adicionado a lista: ')))]
c = 0
while c <= 3:
    Lista.append(int(input('Digite cinco valores para ser adicionado a lista: ')))
    c += 1
    while Lista[c] in Lista[:c]:
        Lista[c] = (int(input(f'Por favor, não digite valores repetidos. Digite um valor diferente de {Lista[c]}: ')))
print(f'Você digitou os valores: ', end='')
Lista = sorted(Lista)
print(*Lista, sep=", ")
