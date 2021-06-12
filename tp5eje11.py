################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def promedio_movil(lista, shift):
    promedios = []

    flag = shift-1
    divisor = shift

    maximo = len(lista)

    for i in range(0,maximo):
        suma = 0

        if flag>=maximo:
            flag = len(lista)
            divisor-=1
        else:
            flag+=1
        
        for x in range(i, flag):
            suma+=lista[x]
        
        promedio = suma/divisor
        promedios.append(promedio)


    return promedios    


def prueba():
    lista = [0.094,0.761,0.977,0.811,0.865,0.61,0.875]
    ventana = int(input('Ingrese ventana: '))

    promedio = promedio_movil(lista, ventana)

    print(promedio)



if __name__ == '__main__':
    prueba()