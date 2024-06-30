################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def numero_perfecto(num):
    suma = 0
    for x in range(1,num):
        if num%x == 0:
            suma+=x
    
    if num == suma:
        return 1
    else:
        return 0



def prueba():
    try:
        numero = int(input('Ingrese numero: '))
    except ValueError:
        print('No es un numero')
    
    if numero_perfecto(numero) == 1:
        print(f'{numero} es un numero perfecto')
    else:
        print(f'{numero} no es un numero perfecto')



if __name__ == '__main__':
    prueba()