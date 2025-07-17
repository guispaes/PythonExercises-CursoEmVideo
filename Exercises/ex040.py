Nota1 = float(input('Primeira nota do Aluno(a): '))
Nota2 = float(input('Segunda nota do Aluno(a): '))
Media = (Nota1+Nota2)/2
print(f'Tirando {Nota1:.1f} e {Nota2:.1f}, a média é {Media:.1f}')
if Media < 5.0:
    print('O aluno foi REPROVADO!')
elif Media >= 7.0:
    print('O aluno foi APROVADO!')
else:
    print('O aluno está de RECUPERAÇÃO!')