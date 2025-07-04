from math import sin, cos, tan, radians
Angulo = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {Angulo:.2f} tem o Seno de {sin(radians(Angulo)):.2f}\n'
      f'O ângulo de {Angulo:.2f} tem o Cosseno de {cos(radians(Angulo)):.2f}\n'
      f'O ângulo de {Angulo:.2f} tem a Tangente de {tan(radians(Angulo)):.2f}')
