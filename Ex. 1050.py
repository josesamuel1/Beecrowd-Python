from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

ddd = {
    11: 'Sao Paulo',
    19: 'Campinas',
    21: 'Rio de Janeiro',
    27: 'Vitoria',
    31: 'Belo Horizonte',
    32: 'Juiz de Fora',
    61: 'Brasilia',
    71: 'Salvador'
} # Dicionário contendo as
  # informações da questão.

def fnc1 (ddd):
    opr = int (input ())
    # Atribuição de valor.
    
    fnc2 (ddd, opr)
    # Chama a função para ser executada.

def fnc2 (ddd, opr):
    for code, city in ddd.items():
        if opr in ddd:
            if opr == code:
                print (city)
                break
                # Caso o 'opr' esteja contido no
                # dicionário e seja igual ao 'code',
                # irá imprimir o nome da cidade.
        else:
            print ('DDD nao cadastrado')
            break
            # Caso o 'opr' não esteja contido
            # no dicionário, irá imprmir a
            # respectiva frase.

fnc1 (ddd)
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# ddd = int(input())
#
# if ddd == 11:
#     print ('Sao Paulo')
#
# elif ddd == 19:
#     print ('Campinas')
#
# elif ddd == 21:
#     print ('Rio de Janeiro')
#
# elif ddd == 27:
#     print ('Vitoria')
#
# elif ddd == 31:
#     print ('Belo Horizonte')
#
# elif ddd == 32:
#     print ('Juiz de Fora')
#
# elif ddd == 61:
#     print ('Brasilia')
#
# elif ddd == 71:
#     print ('Salvador')
#
# else:
#     print ('DDD nao cadastrado')