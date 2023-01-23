from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def kpl (t, v):
    return (t * v) / 12
    # Função que retorna a distância
    # média por litro no automóvel.
    
def fnc1 ():
    t = int (input ())
    v = int (input ())
    # Atribuição de valores.
    
    print (f'{kpl (t, v):.3f}')
    # Comando função e impressão que
    # retorna o consumo do automóvel.
    
fnc1 ()
# Chama a função para ser executada.