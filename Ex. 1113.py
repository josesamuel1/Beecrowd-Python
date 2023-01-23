from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

while 1:
    # Código de laço infinito até que um
    # comando de parada seja executado.
    
    x, y = map (int, input().split())
    # Atribuição de valores.

    if x == y:
        break
        # Caso 'x' e 'y' são iguais.
    
    if x > y:
        print ('Decrescente')
        # Caso onde 'x' é maior que 'y'.
    
    if x < y:
        print ('Crescente')
        # Caso onde 'x' é menor que 'y'.