################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def fibonacci(n):
    if n < 2:
        return n
    else:
        a = fibonacci(n-1) + fibonacci(n-2)

    return a

def prueba():
    try:
        n = int(input('Ingrese numero: '))
    except ValueError:
        print('eso no es un numero')
    
    enesimo = fibonacci(n)

    print(enesimo)


if __name__ == "__main__":
    prueba()