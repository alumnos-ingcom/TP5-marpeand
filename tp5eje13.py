################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class ExceptionWord(Exception):
    pass


def buscar_index(texto, palabra):

    palabra_buscar = ''

    for i in range(len(texto)):
        if palabra[0] == texto[i]:
            index = i
            for x in range(i,(i+len(palabra))):
                palabra_buscar+=texto[x]

            if palabra_buscar == palabra:
                break
            else:
                index = 0
                palabra_buscar = ''

    return index


def buscador(texto, palabra):
    
    if palabra in texto:
        index = buscar_index(texto, palabra)
        return index
    else:
        raise ExceptionWord('Palabra no encontrada')
    

def prueba():
    texto = input('Ingrese texto: ')
    palabra = input('Ingrese palabra: ')

    print(buscador(texto,palabra))


if __name__ == '__main__':
    prueba()