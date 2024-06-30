################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def comparacion(lista1, lista2):
    if len(lista1) == len(lista2):
        lista1.sort()
        lista2.sort()

        i = 0

        for l1 in lista1:
            for l2 in lista2:
                if l1 == l2:
                    i+=1
        
        if i == len(lista1):
            return True
        else:
            return False

    else:
        return False



def prueba():
    lista1 = [1,2,3,4,5,6,7]
    lista2 = [9,6,5,3,4,1,1]

    print(comparacion(lista1, lista2))



if __name__ == '__main__':
    prueba()