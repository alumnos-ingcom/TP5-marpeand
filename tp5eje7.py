################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia(numero1, numero2):
    distan = min(numero1,numero2)- max(numero1,numero2)
    
    if distan < 0:
        return -distan
    else:
        return distan


def prueba():
    num1 = int(input('Ingrese numero: '))
    num2 = int(input('Ingrese otro numero: '))

    dist = distancia(num1, num2)
    print(f'la distancia entre {num1} y {num2} es {dist}')




if __name__ == '__main__':
    prueba()