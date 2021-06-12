################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def inversion(palabra):
    palabra_invertida = ''
    for i in palabra:
        if i.isupper() == True:
            palabra_invertida+=i.lower()
        else:
            palabra_invertida+=i.upper()

    return palabra_invertida

def prueba():

    string = input('Ingrese palabra a invertir: ')
    invertida = inversion(string)
    print(invertida)


if __name__ == "__main__":
    prueba()