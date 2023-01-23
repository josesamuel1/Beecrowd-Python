from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

cond = 1
# Atribuição de valor para condição.

while cond == 1:
    # Comando de laço infinito até que um
    # comando de parada seja executado.

    n1 = float (input ())
    # Atribuição de valor.

    while n1 < 0 or n1 > 10:
        print ('nota invalida')
        n1 = float (input ())
        # Condição onde somente aceitará
        # notas inseridas entre 0 e 10.

    n2 = float (input ())
    # Atribuição de valor.

    while n2 < 0 or n2 > 10:
        print ('nota invalida')
        n2 = float (input ())
        # Condição onde somente aceitará
        # notas inseridas entre 0 e 10.
        
    print (f'media = {(n1 + n2) / 2:.2f}')
    # Impressão das médias do aluno com
    # base nos dados inseridos pelo usuário.

    print ('novo calculo (1-sim 2-nao)')
    cond = int (input ())
    # Atribuição de valor condicional, para saber
    # se o código deve continuar sendo executado.

    while cond < 1 or cond > 2:
        print ('novo calculo (1-sim 2-nao)')
        cond = int (input ())
        # Caso onde a condição dada não seja
        # nenhuma das oferecidas pelo usuário.

# # # # # # # # # # # # # # #

# cond = 1
#
# while cond == 1:
#     n1 = float (input ())
#
#     while n1 < 0 or n1 > 10:
#         print ('nota invalida')
#         n1 = float (input ())
#
#     n2 = float (input ())
#
#     while n2 < 0 or n2 > 10:
#         print ('nota invalida')
#         n2 = float (input ())
#
#     media = (n1 + n2) / 2
#     print (f'media = {media:.2f}')
#
#     print ('novo calculo (1-sim 2-nao)')
#     cond = int (input ())
#
#     while cond < 1 or cond > 2:
#         print ('novo calculo (1-sim 2-nao)')
#         cond = int (input ())