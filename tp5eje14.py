################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def capicua(num):
    inverso = ''
    numero = str(num)

    for i in reversed(numero):
        inverso+=i

    if numero == inverso:
        return True
    else:
        return False

    



def prueba():
    numero = int(input('Ingrese el primer numero: '))
    print(capicua(numero))

if __name__ == '__main__':
    prueba()