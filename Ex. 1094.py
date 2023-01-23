from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    rep = int (input ())
    # Atribuição de valores para contagem
    
    fnc2 (rep)
    # Chama a função para ser executada.

def fnc2 (rep):
    c = r = s = total = 0
    # Atribuição de valores para contagem.
    
    for _ in range (rep):
        qntd, tipo = input().split()
        # Atribuição de valores.
    
        qntd = int (qntd)
        tipo = str (tipo)
        # Casting de variáveis.
    
        if tipo == 'C':
            c += qntd
            total += qntd
        if tipo == 'R':
            r += qntd
            total += qntd
        if tipo == 'S':
            s += qntd
            total += qntd
        # Condições para contagem de entradas
        # inseridas pelo usuário.

    p_c = (c / total) * 100
    p_r = (r / total) * 100
    p_s = (s / total) * 100
    # Cálculo para a porcentagem de entradas.

    print (f'Total: {total} cobaias')
    print (f'Total de coelhos: {c}')
    print (f'Total de ratos: {r}')
    print (f'Total de sapos: {s}')
    print (f'Percentual de coelhos: {p_c:.2f} %')
    print (f'Percentual de ratos: {p_r:.2f} %')
    print (f'Percentual de sapos: {p_s:.2f} %')
    # Impressão de valores.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# rep = int (input ())
#
# c = r = s = total = 0
#
# for _ in range (0, rep):
#     qntd, tipo = input().split()
#     qntd = int (qntd)
#     tipo = str (tipo)
#
#     if tipo == 'C':
#         c += qntd
#         total += qntd
#     if tipo == 'R':
#         r += qntd
#         total += qntd
#     if tipo == 'S':
#         s += qntd
#         total += qntd
#
# p_c = (c / total) * 100
# p_r = (r / total) * 100
# p_s = (s / total) * 100
#
# print (f'Total: {total} cobaias')
# print (f'Total de coelhos: {c}')
# print (f'Total de ratos: {r}')
# print (f'Total de sapos: {s}')
# print (f'Percentual de coelhos: {p_c:.2f} %')
# print (f'Percentual de ratos: {p_r:.2f} %')
# print (f'Percentual de sapos: {p_s:.2f} %')