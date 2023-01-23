from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

maior = cont = 0
# Atribuição de valores para contagem
while cont < 100:
    cont += 1
    # Atribuição de valor para contagem.
    
    num = int (input ())
    # Atribuição de valor.
    
    if num >= maior:
        maior = num
        pos = cont
        # Caso 'num' seja maior que 'maior'
        # irá reatribuir seu valor e sua
        # posição 'pos' atual.
        
print (maior)
print (pos)
# Impressão de valores.