import time
import os

def obtener_nombre_archivo():
    ''' Devuelve una cadena con el nombre de archivo de salida con el
    formato resultados_MMDD_HHSSMM.txt, correspondiente a la fecha y hora
    actual del sistema.
    '''
    return "resultados_" + time.strftime("%m%d_%H%M%S") + ".txt"


def exportar_resultados(resultados, cabecera, descripcion):
    ''' Graba en un archivo una descripción de la consulta realizada y los
    resultados en forma tabulada, agregando la cabecera correspondiente.
        Descripción debe ser una cadena descriptiva de la consulta
    realizada. Cabecera debe ser una tupla con el contenido de cada columna
    que va a tener la tabla de salida. Resultados debe ser una lista de
    tuplas.
        Devuelve el nombre del archivo que se grabó.
    '''

    #Obtengo el nombre del arhivo y lo abro en modo escritura.
    nombre_archivo = obtener_nombre_archivo()
    file=open(nombre_archivo, 'w')

    #Escribo el archivo.
    file.write(descripcion + '\n\n')
    for c in cabecera:
        file.write(c + '     ')
    file.write('\n')
    #Recorro los resultados y escribo el primer elemeto.
    for elemento in resultados:
        file.write(elemento[0])
        #Si el largo es mayor a 1 el resultado tiene dos elementos y escribo
        #el segundo
        if len(elemento) > 1:
            file.write('     ' + elemento[1])
        file.write('\n')
    file.close()

    return nombre_archivo
