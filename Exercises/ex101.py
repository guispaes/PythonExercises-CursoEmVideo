def voto(ano_de_nascimento):
    """
    Lê o ano de nascimento e retorna se a pessoa nascida nesse ano pode votar ou não!
    :param ano_de_nascimento: Ano de nascimento
    :return: n/d
    """
    from datetime import date
    idade = date.today().year - ano_de_nascimento
    if idade<16:
        print(f'Aos {idade} anos de idade: Não vota!')
    elif 16<idade<18:
        print(f'Aos {idade} anos de idade: Voto opcional!')
    elif 18<=idade<70:
        print(f'Aos {idade} anos de idade: Voto obrigatório!')
    else:
        print(f'Aos {idade} anos de idade: Voto opcional!')


voto(int(input('Ano de nascimento: ')))
