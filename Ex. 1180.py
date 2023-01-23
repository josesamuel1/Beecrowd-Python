from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def ident_menor (vetor, tam):
    menor = int (vetor[0])
    # Atribuição de valor.
    
    for i in range (tam):
        if menor > int (vetor[i]):
            menor = int (vetor[i])
            pos = i
    
    print (f'Menor valor: {menor}')
    print (f'Posicao: {pos}')
    # Impressão de valores.
    
    # Função que irá analisar todos os números em
    # 'vetor' e irá imprimir o menor valor e sua posição.

def dados_vetor ():
    tam = int (input ())
    vetor = input().split()
    # Atribuição de valores.
    
    ident_menor (vetor, tam)
    # Chama a função para ser executada.

dados_vetor ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# tam = int (input ())
# vetor = input().split()
# menor = int (vetor[0])
# pos = cont = 0
#
# while cont < tam:
#     if menor > int(vetor[cont]):
#         menor = int(vetor[cont])
#         pos = cont
#
#     cont += 1
#
# print (f'Menor valor: {menor}')
# print (f'Posicao: {pos}')