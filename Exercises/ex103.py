def ficha(nome_jogador, quantidade_gols):
    """
    Exibe o jogador e quantidade de gols que ele fez.
    
    nome_jogador: Nome do jogador.
    quantidade_gols:  Quantidade de gols do jogador.
    return: Nenhum retorno, apenas imprime na tela.
    """

    if nome_jogador == "": nome_jogador = "<desconhecido>"
    if quantidade_gols == "": quantidade_gols = "0"
    print(f'O {nome_jogador} marcou {quantidade_gols} gol(s) no campeonato.')


#Atribuição de váriaveis
jogador = str(input("Nome do jogador: ").strip().title())
while not jogador.replace(" ", "").isalpha() and jogador != "":
    jogador = str(input(f"O nome do jogador deve conter apenas letras!\nNome do jogador: ").strip().title())
gols = str(input("Quantos gols ele marcou? "))
while not gols.isdigit() and gols != "":
    gols = str(input(f"A quantidade de gols deve ser númerica!\nQuantos gols ele marcou? ").strip())

#Função
ficha(jogador, gols)
