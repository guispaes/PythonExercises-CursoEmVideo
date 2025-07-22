Alunos = [[], [], [], []]
Contador = int(0)

#Código
while True:
    Alunos[0].append(str(input('Nome: ').title()))
    Alunos[1].append(float(input('Nota 1: ')))
    Alunos[2].append(float(input('Nota 2: ')))
    Alunos[3].append(float((Alunos[1][Contador]+Alunos[2][Contador])/2))
    Continuar = str(input('Quer continuar[S/N]? ').upper())
    Contador += 1
    if Continuar != 'S' and Continuar != 'N':
        Continuar = str(input('Por favor, digite uma resposta válida. Quer continuar[S/N]? ')).upper()
    elif Continuar == 'N':
        break

#Mostra o boletim
print(f'{'N°':<5}{'Nome':<40}Média')
print(50*"-")
for c in range(0, len(Alunos[0])):
    print(f'{c:<5}{Alunos[0][c]:<40}{Alunos[3][c]:.1f}')

while True:
    Notas = int(input(f'\n{'MOSTRAR NOTAS DO ALUNO':^50}\n'
                      f'{'Utilize o índice a esquerda para a seleção':^50}\n'
                      f'{'Utilize o índice n°999 para interromper o programa':^50}\n'
                      f'? '))
    if Notas == 999:
        break
    elif Notas > len(Alunos[0])-1:
        Notas = int(input('Por favor, digite uma resposta válida.\n '
                          '? '))
    else:
        print(f'\nNotas de {Alunos[0][Notas]}: {Alunos[1][Notas]}, {Alunos[2][Notas]}')
        continue
