# EXERCÍCIO 1: FAÇA UM PROGRAMA QUE PEÇA UM VALOR MONETÁRIO E DIMINUA-O EM 15%. SEU PROGRAMA DEVE IMPRIMIR A MENSAGEM: ' O NOVO VALOR É [VALOR]'.
monetario = float(input('Entre com um valor monetário: '))
valor = monetario - (monetario * 0.15)
print('O novo valor é: ', valor)