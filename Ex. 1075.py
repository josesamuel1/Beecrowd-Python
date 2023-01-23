from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

x = int (input ())
# Atribuição de valor.

resto = 1
# Atribuição de valor para contagem.

while resto < 10000:
    if resto % x == 2:
        print (resto)

    resto += 1
    # Condição que irá imprimir
    # todos os números que divididos
    # por 'x' dêem resto igual a 2.

# # # # # # # # # # # # # # #

# x = int (input ())
#
# for resto in range (10001):
#     if resto % x == 2:
#         print (resto)