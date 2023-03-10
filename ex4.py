'''Faça um programa que converta da notação de 24 horas
para a notação de 12 horas. Por exemplo, o programa deve
converter 14:25 em 2:25 P.M. A entrada é dada em dois
inteiros. Deve haver pelo menos duas funções: uma para fazer
a conversão e uma para a saída. Registre a informação
A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a
função para efetuar as conversões terá um parâmetro formal
para registrar se é A.M. ou P.M. Inclua um loop que permita que
o usuário repita esse cálculo para novos valores de entrada
todas as vezes que desejar.'''
import os

hora = int(input('Inofrme a hora: '))
minuto = int(input('Informe os minutos: '))


def converter_hora(hora):
    return (hora -12)

def imprime_hora(hora,minuto):
    if(hora <= 12):
        print(hora,':',minuto,'AM')
    else:
        print(converter_hora(hora),':', minuto, 'PM')
    os.system('cls')
    os.system(('pause'))
imprime_hora(hora, minuto)

es=''

while es != 2:
    print('1-Converter novamente ')
    print('2-Sair')
    op=int(input('Esolha a opção '))
    if op == 1:

        hora = int(input('Informe a hora: '))
        minuto = int(input('Informe os minutos: '))


        def converter_hora(hora):
            return (hora - 12)


        def imprime_hora(hora, minuto):
            if hora <= 12:
                print(hora, minuto, 'AM')
            else:
                print(converter_hora(hora),':', minuto, 'M')
            os.system('cls')
            os.system(('pause'))
        imprime_hora(hora, minuto)
    elif op == 2:
        print('FIM')
        break