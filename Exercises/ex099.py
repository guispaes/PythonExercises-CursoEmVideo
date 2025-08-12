def maior(valores):
    maior_valor = valores[0]
    for c in range(len(valores)):
        if valores[c] > maior_valor:
            maior_valor = valores[c]
    return maior_valor

lista_valores = [1,4,8]
print(f'Analisando os valores: {lista_valores}:\n'
      f'Foram informados {len(lista_valores)} valores ao todo.\n'
      f'O maior valor informado foi {maior(lista_valores)}')