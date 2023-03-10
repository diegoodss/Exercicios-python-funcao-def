'''Faça um programa, com uma função que
necessite de um argumento. A função retorna o
valor de caractere ‘P’, se seu argumento for
positivo, e ‘N’, se seu argumento for zero ou
negativo.'''

def arg (n1):
    numero=float(n1)
    if numero <=0:
        print('Negativo')
    else:
        print('Positivo')
arg()