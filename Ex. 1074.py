from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def detector (num):
    if num == 0:
        print ('NULL')
    elif num > 0:
        if num % 2 == 0:
            print ('EVEN POSITIVE')
        else:
            print ('ODD POSITIVE')
    elif num < 0:
        if num % 2 == 0:
            print ('EVEN NEGATIVE')
        else:
            print ('ODD NEGATIVE')
    # Função que irá detectar se 'num' é par,
    # ímpar ou nulo, positivo ou negativo.
    # Depois irá imprimir a respectiva mensagem.
    
def fnc1 ():
    rep = int (input ())
    # Atribuição de valor para contagem.

    for _ in range (rep):
        num = int (input ())
        # Atribuição de valor.

        detector (num)
        # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.