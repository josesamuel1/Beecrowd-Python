from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fatorial (num):
    # Função fatorial com recursividade.

    if num < 2:
        return 1
    else:
        return num * fatorial (num - 1)

print (fatorial (int (input ())))
# Chamada e impressão de fatorial
# do número inserido pelo usuário.

# # # # # # # # # # # # # # #

# fat = 1
# x = int (input ())
#
# while x > 0:
#     fat *= x
#     x -= 1
#
# print (fat)

# fat = 1
# x = int (input ())
#
# for i in range (1, x + 1):
#     fat *= i
#
# print (fat)