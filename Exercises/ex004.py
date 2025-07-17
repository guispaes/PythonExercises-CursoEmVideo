word1 = str(input('Digite algo: '))
print(
      f'O tipo primitivo desse valor é: {type(word1)}\n'
      f'Só tem espaços? {word1.isspace()}\n'
      f'É um número? {word1.isnumeric()}\n'
      f'É alfabético? {word1.isalpha()}\n'
      f'É alfanumérico? {word1.isalnum()}\n'
      f'Está em maiúsculas? {word1.isupper()}\n'
      f'Está em minúsculas? {word1.islower()}\n'
      f'Está capitalizada? {word1.istitle()}'
     )
