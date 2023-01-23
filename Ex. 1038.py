from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

pedidos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
} # Dicionário contendo os dados da questão.

def fazendo_pedido (pedidos):
    code, qntd = map (int, input().split())
    # Atribuição de valores.
    
    for key, value in pedidos.items():
        if key == code:
            total = value * qntd
    # Caso onde irá procurar o código
    # do alimento e informar o valor total
    # do produto multiplicado pelo preço.
    
    print (f'Total: R$ {total:.2f}')
    # Impressão de valor.

fazendo_pedido (pedidos)
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# def fnc1 ():
#     code, espec = map (int, input().split())
#
#     pedidos(code, espec)
#
# def pedidos (code, espec):
#     if code == 1:
#         total = 4.00 * espec
#
#     if code == 2:
#         total = 4.50 * espec
#
#     if code == 3:
#         total = 5.00 * espec
#
#     if code == 4:
#         total = 2.00 * espec
#
#     if code == 5:
#         total = 1.50 * espec
#
#     print(f'Total: R$ {total:.2f}')
#
# fnc1 ()

# x = input().split()
#
# cod, espec = x
# espec = float (espec)
#
# if cod == '1':
#     total = 4.00 * espec
#     print(f"Total: R$ {total:.2f}")
#
# if cod == '2':
#     total = 4.50 * espec
#     print(f"Total: R$ {total:.2f}")
#
# if cod == '3':
#     total = 5.00 * espec
#     print(f"Total: R$ {total:.2f}")
#
# if cod == '4':
#     total = 2.00 * espec
#     print(f"Total: R$ {total:.2f}")
#
# if cod == '5':
#     total = 1.50 * espec
#     print(f"Total: R$ {total:.2f}")