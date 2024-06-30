################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def entero_binario(entero):
    binario = ''

    while entero // 2 !=0:
        Nbin = entero%2
        binario = str(Nbin) + binario
        entero = entero // 2
    
    return str(entero) + binario


def binario_entero(Nbinario):
    suma = 0
    binario = str(Nbinario)
    l = len(binario)
    i = 0

    for x in reversed(range(l)):
        suma = suma + (int(binario[i]) * (2**x))
        i+=1
    
    return suma

        
def prueba():
    numero = int(input('Ingrese numero: '))
    print(entero_binario(numero))
    bina = int(input('Ingrese numero binario: '))
    print(binario_entero(bina))



if __name__ == '__main__':
    prueba()