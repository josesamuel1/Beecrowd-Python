from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    a = int (input ())
    b = int (input ())
    c = int (input ())
    d = int (input ())
    # Atribuição de valores.

    print (f'DIFERENCA = {calc (a, b, c, d)}')
    # Comando função e impressão que
    # retorna a diferença dos valores.

def calc (a, b, c, d):
    return a * b - c * d
# Função que retorna a diferença dos
# números inseridos pelo usuário.

fnc1 ()
# Chama a função para ser executada.