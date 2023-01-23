from os import system
# Livraria 'os/system'.
system ('cls')
# Limpa o terminal.

def fnc1 ():
    n1, n2, n3, n4 = map (float, input().split())
    # Atribuição de valores.
    
    print (f'Media: {medianotas (n1, n2, n3, n4):.1f}')
    # Comando função e impressão que
    # retorna a média de notas do aluno.
    
    if medianotas (n1, n2, n3, n4) >= 7:
        print ('Aluno aprovado.')
        # Caso a média das notas
        # seja maior ou igual a 7.
        
    elif medianotas (n1, n2, n3, n4) < 5:
        print ('Aluno reprovado.')
        # Caso a média das notas
        # seja menor que 5.
        
    elif 5 <= medianotas (n1, n2, n3, n4) <= 6.9:
        print ('Aluno em exame.')
        exame = float (input())
        # Atribuição de valor.
        
        print (f'Nota do exame: {exame:.1f}')
        # Caso a média das notas do aluno
        # esteja entre 5 e 6.9.
        
        if novamedia (medianotas (n1, n2, n3, n4), exame) >= 5:
            print ('Aluno aprovado.')
            print (f'Media final: {novamedia (medianotas (n1, n2, n3, n4), exame):.1f}')
            # Caso a nova média do aluno
            # seja maior ou igual a 5.
        else:
            print ('Aluno reprovado.')
            print (f'Media final: {novamedia (medianotas (n1, n2, n3, n4), exame):.1f}')
            # Caso a nova média do aluno
            # seja menor que 5.

def medianotas (n1, n2, n3, n4):
    return ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
    # Função que retorna a média do aluno com base nas notas inseridas.

def novamedia (media, exame):
    return (media + exame) / 2
    # Função que retorna a nova média do aluno depois de outro exame.

fnc1 ()
# Chama a função para ser executada.

# # # # # # # # # # # # # # #

# n1, n2, n3, n4 = map (float, input().split())
#
# media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
# print (f"Media: {media:.1f}")
#
# if media >= 7.0:
#     print ("Aluno aprovado.")
#
# elif media < 5.0:
#     print ("Aluno reprovado.")
#
# elif 5.0 <= media <= 6.9:
#     print ("Aluno em exame.")
#
#     exame = float(input())
#     print (f"Nota do exame: {exame:.1f}")
#
#     novamedia = (media + exame) / 2
#     if novamedia >= 5.0:
#         print ("Aluno aprovado.")
#         print (f"Media final: {novamedia:.1f}")
#     else:
#         print ("Aluno reprovado.")
#         print (f"Media final: {novamedia:.1f}")