from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

while 1:
    # Comando de laço infinito até que um
    # comando de parada seja executado.

    x, y = map (int, input().split())
    # Atribuição de valores.
    
    if x == 0 or y == 0:
        break
        # Condição de parada caso 'x'
        # ou 'y' seja igual a 0.

    if x > 0:
        if y > 0:
            print ('primeiro')
        else:
            print ('quarto')
            
    elif x < 0:
        if y > 0:
            print ('segundo')
        else:
            print ('terceiro')
    # Casos onde detectará em que
    # quadrante o ponto se encontra.