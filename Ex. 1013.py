from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def maiornumero (a, b, c):
    x = (a + b + abs(a - b)) / 2
    maior = (x + c + abs(x - c)) / 2
    return maior
    # Função que retornará sempre o maior
    # valor inserido pelo usuário.

def fnc1 ():
    a, b, c = map (int, input().split())
    # Atribuição de valores.
    
    print (f'{maiornumero (a, b, c)} eh o maior')
    # Comando função e impressão que
    # retorna o maior número.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# a, b, c = map (int, input().split())
#
# x = (a + b + abs(a - b)) / 2
# maior = (x + c + abs(x - c)) / 2
#
# print(f'{maior} eh o maior')