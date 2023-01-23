from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    rep = int (input ())
    # Atribuição de valor para contagem.,
    
    fnc2 (rep)
    # Chama a função para ser executada.

def fnc2 (rep):
    vetor = [0, 1]
    a = 0
    b = 1
    # Atribuição de valores.

    for _ in range (rep):
        x = int (input ())
        # Atribuição de valor para contagem.
        
        if x > 2:
            for _ in range (x):
                fib = a + b
                a = b
                b = fib
                # Cálculo da sequência de fibonacci.
                
                vetor.append (fib)
                # Insere o valor no vetor.
                
            print (f'Fib({x}) = {vetor[x]}')
            # Caso a condição seja verdadeira.

        else:
            print (f'Fib({x}) = {vetor[x]}')
            # Caso contrário.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# rep = int (input ())
# vetor = [0, 1]
# a = 0
# b = 1
#
# for _ in range (rep):
#     x = int (input ())
#
#     if x > 2:
#         for _ in range (x):
#             fib = a + b
#             a = b
#             b = fib
#             vetor.append (fib)
#
#         print (f'Fib({x}) = {vetor[x]}')
#
#     else:
#         print (f'Fib({x}) = {vetor[x]}')