################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def par_impar(numero):
    num = numero
    
    if (num//2)*2 == num:
        return 'es par'
    else:
        return 'es impar'


def prueba():
    try:
        num = int(input('Ingrese un numero: '))
    except ValueError:
        print('eso no es un numero')

    res = par_impar(num)
    print(res)

if __name__ == "__main__":
    prueba()