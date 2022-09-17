'''
Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não.

    a - Mora perto da vítima?
    b - Já trabalhou com a vítima?
    c - Telefonou para a vítima?
    d - Esteve no local do crime?
    e - Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 e 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações.
valores iguais ou abaixo de 1 são liberados.
'''

pergunta_1 = input('Mora perto da vítima?').lower() == 'sim'
pergunta_2 = input('Já trabalhou com a vítima?').lower() == 'sim'
pergunta_3 = input('Telefonou para a vítima?').lower() == 'sim'
pergunta_4 = input('Esteve no local do crime?').lower() == 'sim'
pergunta_5 = input('Devia para a vítima?').lower() == 'sim'

pontos = pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5

if pontos == 5:
    print('Assassino')
elif pontos == 4 or pontos == 3:
    print('Cumplíces')
elif pontos == 2:
    print('Suspeito')
else:
    print('Liberado')