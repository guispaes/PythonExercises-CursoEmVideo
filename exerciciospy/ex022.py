Nome1 = str(input('Digite seu nome completo: ').strip())
Nome2 = Nome1.split()
print(f'Analisando seu nome: \n'
      f'Seu nome em maiúsculas é {Nome1.upper()}\n)'
      f'Seu nome em minúsculas é {Nome1.lower()}\n'
      f'Seu nome tem ao todo {len(Nome1.replace(' ', ''))} letras\n'
      f'Seu primeiro nome é {Nome2[0]} e ele tem {len(Nome2[0])}\n')
