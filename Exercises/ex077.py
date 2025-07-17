Tupla = ('Palavra', 'Livro', 'Mercado', 'Papel')

for c in Tupla:
  print(f'Em {c} temos:', end=' ')
  for Vogal in c:
    if Vogal in 'aeiou':
      print(Vogal, end=' ')
  print()
 
