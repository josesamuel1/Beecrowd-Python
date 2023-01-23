from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def delta (a, b, c):
    return b**2 - 4 * a * c
    # Função que retornará o valor de delta.

def bhaskara (a, b, delta):
    r1 = (-b + (delta)**0.5) / (2 * a)
    r2 = (-b - (delta)**0.5) / (2 * a)
    # Calcula e armazena os valores nas variáveis.
    
    if r1 == r2:
        print (f'R1 = {r1:.5f}')
        # Condição caso 'R1' e 'R2' sejam iguais.
    else:
        print (f'R1 = {r1:.5f}')
        print (f'R2 = {r2:.5f}')
        # Condição caso 'R1' e 'R2' não sejam iguais.

def fnc1 ():
    a, b, c = map (float, input().split())
    # Atribuição de valores.
    
    if a != 0:
        d = delta (a, b, c)
        # Caso 'a' seja diferente de 0.
        
        if d >= 0:
            bhaskara(a, b, d)
            # Caso 'd' seja maior ou igual a 0.
            
        else:
            print ("Impossivel calcular")
    else:
        print ("Impossivel calcular")

fnc1 ()
# Chama a função para ser executada.