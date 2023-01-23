from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1145:
nums, max = map (int, input().split())
# Atribuição de valores.

numsi = nums
# Caso que identificará até quantos números
# deverá ser impresso em uma única linha.

for i in range (1, max + 1):
    if i < nums:
        print (i, end=' ')
    else:
        print (i) #!!! NÃO DEVE HAVER ESPAÇO NO FINAL
        nums += numsi
        # Comando de repetição que, para cada linha,
        # irá imprimir de 1 até 'max' com 'nums' caracteres
        # em cada linha, até que 'max' seja imprimido.

# EXEMPLO 1146:
# x = 1
# # Atribuição de valor.
#
# while x != 0:
#     # Comando de laço infinito até que um
#     # comando de parada seja executado.
#   
#     x = int (input ())
#     # Atribuição de valor.
#
#     for i in range (1, x + 1):
#         if i == x:
#             print (i)
#         else:
#             print (i, end=' ')
#             # O comando irá imprimir, em
#             # cada linha, de 1 até 'x',
#             # até que 0 seja inserido.