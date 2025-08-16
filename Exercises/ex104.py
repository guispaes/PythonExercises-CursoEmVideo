def leiaint(mensagem):
    """
    Solicita ao usuário a entrada de um número inteiro, repetindo até que uma entrada válida seja fornecida.
    
    mensagem: Texto a ser exibido no prompt de entrada.
    return: Número digitado pelo úsuario.
    """
    numero_inteiro = str(input(f"{mensagem}").replace(" ", ""))
    while not (numero_inteiro.isdigit() or (numero_inteiro.startswith(("-", "+")) and numero_inteiro[1:].isdigit())):
        numero_inteiro = str(input(f"ERRO! Digite um número inteiro.\n{mensagem}").replace(" ", ""))
    numero_inteiro = int(numero_inteiro)
    return numero_inteiro

numero = leiaint('Digite um número: ') 
print(f"Você acabou de digitar o número {numero}")
