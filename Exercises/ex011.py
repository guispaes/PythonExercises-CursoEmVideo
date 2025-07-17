#2.m2 = 1l de tinta
Altura = float(input('Altura da parede: '))
Largura = float(input('Largura da parede: '))
MetroQuadrado = Altura*Largura
print(f'Sua parede possui {MetroQuadrado:.2f}m²\n'
      f'Você precisará de: {MetroQuadrado/2:.2f}L de tinta\n'
      f'Tendo em vista que 1L de tinta pode pintar 2m²\n')
