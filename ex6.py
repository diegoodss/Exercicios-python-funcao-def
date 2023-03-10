'''Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.'''

def digitos(d):
    return  len(str(d))
def informe():
    d = int(input('Informe um numero inteiro: '))
    print('A quantidade de Digitos são: ',digitos(d))
while True:
    informe()