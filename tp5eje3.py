################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def tribonacci(n):
    if n < 2:
        return 0
    elif n == 3:
        return 1
    else:
        a = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

    return a

def prueba():
    try:
        n = int(input('Ingrese numero: '))
    except ValueError:
        print('eso no es un numero')
    
    enesimo = tribonacci(n)

    print(enesimo)


if __name__ == "__main__":
    prueba()