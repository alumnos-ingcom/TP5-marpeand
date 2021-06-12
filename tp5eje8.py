################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################



def cifrado(palabra, desplazamiento):
    cifrado = ''

    for x in palabra:
        if x.islower() is True:
            posX = ord(x) - 97
            Ord = (posX + desplazamiento)%26 + 97
            Xcifrado = chr(Ord)
            cifrado+=Xcifrado
        elif x.isupper() is True:
            posX = ord(x) - 65
            Ord = (posX + desplazamiento)%26 + 65
            Xcifrado = chr(Ord)
            cifrado+=Xcifrado
        

    return cifrado

def descifrado(palabra, desplazamiento):
    descifra = ''

    for x in palabra:
        if x.islower() is True:
            posX = ord(x) - 97
            Ord = (posX - desplazamiento)%26 + 97
            Xdescifrado = chr(Ord)
            descifra+=Xdescifrado
        elif x.isupper() is True:
            posX = ord(x) - 65
            Ord = (posX - desplazamiento)%26 + 65
            Xdescifrado = chr(Ord)
            descifra+=Xdescifrado

    return descifra



def prueba():
    a_cifrar = input('Ingrese palabra a cifrar: ')
    desplazamiento = int(input('Ingrese desplazamiento: '))

    texto_cifrado = cifrado(a_cifrar, desplazamiento)
    print(f'palabra cifrada => {texto_cifrado}')

    a_descifrar = input('Ingrese palabra a descifrar: ')
    texto_descifrado = descifrado(texto_cifrado, desplazamiento)
    print(f'palabra descifrada => {texto_descifrado}')



if __name__ == '__main__':
    prueba()