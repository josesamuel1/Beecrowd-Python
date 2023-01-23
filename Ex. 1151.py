from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    fib = int (input ())
    # Atribuição de valor.
    
    fibonacci (fib)
    # Chama a função para ser executada.

def fibonacci (fib):
    a = 0
    b = 1
    # Atribuição de valores.

    for i in range (0, fib - 2):
        x = a + b
        a = b
        b = x

        if i == 0:
            print (i, end=" ")
        if i == 1:
            print (i, end=" ")
        # Sequências de fibonacci predefinidas.

        if i == fib - 3:
            print (x)
        else:
            print (x, end=" ")
        # Sequências de fibonacci de 2 ou mais.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# a = 0
# b = 1
# fib = int (input ())
# # Atribuição de valores.
#
# for i in range (0, fib - 2):
#     x = a + b
#     a = b
#     b = x
#
#     if i == 0:
#         print (i, end=" ")
#     if i == 1:
#         print (i, end=" ")
#     # Sequências de fibonacci predefinidas.
#
#     if i == fib - 3:
#         print (x)
#     else:
#         print (x, end=" ")
#     # Sequências de fibonacci de 2 ou mais.