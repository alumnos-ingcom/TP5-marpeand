################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

factoriones = []

def factorial(numero):

    
    if numero > 1:
        return numero * factorial(numero-1)
    else:
        return 1

def factorion(numero):
    factoriales = []
    suma = 0

    str_num = str(numero)

    for num in str_num:
        factoriales.append(factorial(int(num)))
    
    for Xfact in factoriales:
        suma += Xfact
    
    
    if suma == numero:
        factoriones.append(numero)


def prueba():

    for num in range(14999999):
        factorion(num)

    print(f'factoriones => {factoriones}')


if __name__ == '__main__':
    prueba()