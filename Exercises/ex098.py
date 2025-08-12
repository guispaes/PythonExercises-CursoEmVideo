from time import sleep

def contador(valor, valor_maximo, passo):

    #Analisa o "passo"
    if passo < 0:
        passo = (passo*passo) + passo
    if passo == 0:
        passo += 1

    #Realiza a contagem
    if valor <= valor_maximo:
        while valor <= valor_maximo:
            print(valor, end=' ')
            sleep(0.5)
            valor += passo
    elif valor >= valor_maximo:
        while valor >= valor_maximo:
            print(valor, end=' ')
            sleep(0.5)
            valor -= passo

    #Linha final
    print('Fim!')
    print('-'*30)

contador(1,10, 1)
contador(10, 0, 2)
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))