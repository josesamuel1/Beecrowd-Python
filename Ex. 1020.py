from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def tempo(x):
    ano = x // 365
    x -= ano * 365
    
    mes = x // 30
    x -= mes * 30
    
    dia = x
    return ano, mes, dia
    # Função que retornará os dias em ano, mes e dia.

def fnc1 ():
    x = int (input ())
    ano, mes, dia = tempo (x)
    # Atribuição de valores.

    print (f'{ano} ano(s)')
    print (f'{mes} mes(es)')
    print (f'{dia} dia(s)')
    # Impressão de valores.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# tempo = int (input ())
#
# anos = tempo // 365
# tempo = tempo - anos * 365
#
# meses = tempo // 30
# tempo = tempo - meses * 30
#
# dias = tempo
#
# print (f'{anos} ano(s)')
# print (f'{meses} mes(es)')
# print (f'{dias} dia(s)')