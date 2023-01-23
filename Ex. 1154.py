from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    total = divs = 0
    x = int (input ())
    # Atribuição de valores.

    while x > 0:
        # Condição para que o código sempre seja
        # executado enquanto 'x' for maior que 0.

        total += x
        divs += 1
        x = int (input ())
        # Atribuição de valores.

    mediaidades (total, divs)
    # Chama a função para ser executada.

def mediaidades (total, divs):
    print (f'{total / divs:.2f}')
    # Função que retorna a impressão da média
    # de idades inseridas pelo usuário.

fnc1 ()
# Chama a função para ser executada.