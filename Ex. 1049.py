from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def tipos (tipo1, tipo2, tipo3):
    if tipo1 == 'vertebrado':
        if tipo2 == 'ave':
            if tipo3 == 'carnivoro':
                print ('aguia')
            if tipo3 == 'onivoro':
                print ('pomba')
            
        if tipo2 == 'mamifero':
            if tipo3 == 'onivoro':
                print ('homem')
            if tipo3 == 'herbivoro':
                print ('vaca')

    if tipo1 == 'invertebrado':
        if tipo2 == 'inseto':
            if tipo3 == 'hematofago':
                print ('pulga')
            if tipo3 == 'herbivoro':
                print ('lagarta')
            
        if tipo2 == 'anelideo':
            if tipo3 == 'hematofago':
                print ('sanguessuga')
            if tipo3 == 'onivoro':
                print ('minhoca')
    # Função que irá detectar que
    # animal tem características iguais
    # às que o usuário inseriu.

def fnc1 ():
    tipo1 = str (input ())
    tipo2 = str (input ())
    tipo3 = str (input ())
    # Atribuição de valores.
    
    tipos (tipo1, tipo2, tipo3)
    # Chama a função para ser executada.

fnc1 ()
# Chama a função para ser executada.