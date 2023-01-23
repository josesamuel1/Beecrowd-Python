from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

# EXEMPLO 1046:
def calculo (t1, t2):
    if t1 < t2:
        return t2 - t1
    else:
        return (24 - t1) + t2
    # Função que detecta quantas
    # horas durou a partida.

def fnc1 ():
    t1, t2 = map (int, input().split())
    # Atribuição de valores.

    print (f'O JOGO DUROU {calculo (t1, t2)} HORA(S)')
    # Comando função e impressão que
    # retorna a duração da partida.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# EXEMPLO 1047:
# def fnc1 ():
#     hi, mi, hf, mf = map (int, input().split())
#
#     th, tm = tempodejogo (hi, mi, hf, mf)
#     print (f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
#
# def tempodejogo (hi, mi, hf, mf):
#     if hi < hf:
#         th = hf - hi
#         if mi < mf:
#             tm = mf - mi
#         if mi > mf:
#             th = th - 1
#             tm = (60 - mi) + mf
#         if mi == mf:
#             tm = 0
#
#     if hi > hf:
#         th = (24 - hi) + hf
#         if mi < mf:
#             tm = mf - mi
#         if mi > mf:
#             th = th - 1
#             tm = (60 - mi) + mf
#         if mi == mf:
#             tm = 0
#
#     if hi == hf:
#         if mi < mf:
#             tm = mf - mi
#             th = 0
#         if mi > mf:
#             tm = (60 - mi) + mf
#             th = 23
#         if mi == mf:
#             th = 24
#             tm = 0
#
#     return th, tm
#
# fnc1 ()