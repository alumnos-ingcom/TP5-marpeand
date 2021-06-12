################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def balanceado(string,caracter):
    parentesis_abiertos = 0
    parentesis_cerrados = 0

    for i in string:
        if i == caracter[0] :
            parentesis_abiertos+=1
    
    for x in string:
        if x == caracter[1]:
            parentesis_cerrados+=1
        
    if parentesis_abiertos == 0 and parentesis_cerrados == 0:
        return 0
    elif parentesis_abiertos == parentesis_cerrados:
        return True


def prueba():
    texto = input('Ingrese cadena: ')
    caracter = input('Ingrese caracter a evaluar ()/[]/{} : ')
    result = balanceado(texto, caracter)

    if result:
        print('estan balanceados')
    else:
        print('no estan balanceados')



if __name__ == '__main__':
    prueba()