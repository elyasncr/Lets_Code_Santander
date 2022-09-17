"""
FAÇA UM PROGRAMA QUE LEIA A VALIDADE DAS INFORMAÇÕES:

    A - IDADE: ENTRE 0 E 150;
    B - SALÁRIO: MAIOR QUE 0;
    C - SEXO: M, F OU OUTRO;
O PROGRAMA DEVE IMPRIMIR UMA MENSAGEM DE ERRO PARA CADA INFORMAÇÃO INVÁLIDA.
"""
idade = int(input('Digite o valor da idade: '))
salario = int(input('Digite o seu salário: '))
sexo = input('DIGITE SEU SEXO: ')

if int(idade) <= 150:
    print('Sua idade é ', idade)
else:
    print('Erro. Idade superior a 150.')

if float(salario) > 0:
    print('O seu salário é: ', salario)
else:
    print('Erro. Salário menor que zero.')

if (sexo) =='M':
    print('Seu sexo é: ', sexo)
elif (sexo) =='F':
    print('Seu sexo é: ', sexo)
else:
    print('Erro. Sexo não identificado.')