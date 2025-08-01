def escreva(mensagem):
    espaco = len(mensagem)+4
    print('-'*espaco)
    print(f"{mensagem:^{espaco}}")
    print('-'*espaco)


escreva(str(input('Insira sua mensagem: ').strip().capitalize()) )
