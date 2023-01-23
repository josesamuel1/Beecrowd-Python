from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def condicao (a, b, c, d):
    if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
        return True
        # Caso as condições sejam verdadeiras.

def fnc1 ():
    a, b, c, d = map (int, input().split())
    # Atribuição de valores.
    
    if condicao (a, b, c, d):
        print ('Valores aceitos')
        # Caso a função 'condição' seja verdadeira.
    else:
        print ('Valores nao aceitos')
        # Caso a função 'condição' seja falsa.

fnc1 ()
# Chama a função para ser executada.