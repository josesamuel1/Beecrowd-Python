from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    rep = int (input ())
    # Atribuição de valor para contagem.
    
    equaçao (rep)
    # Chama a função para ser executada.

def equaçao (rep):
    for _ in range (rep):
        soma = 0
        x, y = map (int, input().split())
        # Atribuição de valores.
        
        for _ in range (y * 2):
            if x % 2 == 1:
                soma += x
                # Condição que irá somar todos
                # os números ímpares de 'x' até
                # os próximos 'y' ímpares.
            
            x += 1
            # Atribuição de valor para contagem.
        
        print (soma)
        # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.