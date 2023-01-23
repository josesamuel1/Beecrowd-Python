from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    x = int (input ())
    # Atribuição de valores.
    
    print (f'{dist (x)} minutos')
    # Comando função e impressão que
    # retorna o consumo do automóvel.

def dist (x):
    return x * 2
    # Função que retorna o tempo
    # necessário para a ultrapassagem.
    
fnc1 ()
# Chama a função para ser executada.
