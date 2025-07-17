NomeCidade = str.title(input('Em que cidade você nasceu? ').strip())
Busca = NomeCidade.split()
Resultado = 'Santo' in Busca[0]
print(Resultado)
