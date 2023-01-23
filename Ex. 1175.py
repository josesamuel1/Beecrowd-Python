from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

vetor = []
# Atribuição de valor.

def dados_vetor ():
    for _ in range (20):
        vetor.append (int (input ()))
        # Insere o valor no vetor.

    vetor.reverse ()
    # Comando que reverte todo o vetor.
    
    reverte_vetor (vetor)
    # Chama a função para ser executada.

def reverte_vetor (vetor):
    for i in range (len (vetor)):    
        print (f'N[{i}] = {vetor[i]}')
    
    # Função que irá imprimir
    # todos os valores do vetor.

dados_vetor ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# vetor = []
# i = j = 0
#
# while i < 20:
#
#     vetor.append (int (input ()))
#
#     i += 1
#
# vetor.reverse ()
#
# while j < len (vetor):
#
#     print (f'N[{j}] = {vetor[j]}')
#
#     j += 1