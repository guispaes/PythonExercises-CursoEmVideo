from random import sample
Aluno1 = str(input('Primeiro aluno(a): '))
Aluno2 = str(input('Segundo Aluno(a): '))
Aluno3 = str(input('Terceiro Aluno(a): '))
Aluno4 = str(input('Quarto Aluno(a): '))
print(f'A ordem escolhida é {sample([Aluno1, Aluno2, Aluno3, Aluno4], k = len([Aluno1, Aluno2, Aluno3, Aluno4]))}')
# ou
#from random import shuffle
#Aluno1 = str(input('Primeiro aluno(a): '))
#Aluno2 = str(input('Segundo Aluno(a): '))
#Aluno3 = str(input('Terceiro Aluno(a): '))
#Aluno4 = str(input('Quarto Aluno(a): '))
#lista = [Aluno1, Aluno2, Aluno3, Aluno4]
#shuffle(lista)
#print(f'A ordem escolhida é  {lista}')
