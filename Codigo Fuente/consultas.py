import csv
import itertools

def cargar_archivo(nombre_archivo):
    ''' Recibe el nombre de un archivo y devuelve una estructura de datos
    con su contenido.
        En caso de error levanta una RunnableException con un mensaje
    descriptivo.
    '''
    try:
        #abrimos el archivo y crea el lector para el archivo.
        archivo = open(nombre_archivo)
        #dictreader por si cambia el orden de los campos
        csvReader = csv.DictReader(archivo)

        #genero lista del reader
        lista = list(csvReader)
        archivo.close()
    except OSError as e:
        raise RuntimeError("ERROR: El archivo no existe.")
    #Si pasan las validaciones, devuelve la lista.
    validar_datos(lista)
    return lista

def validar_datos(archivo):
    ''' Realiza todas las validaciones necesarias al archivo para asegurar
    que todas las funcionalidades del programa puedan ejecutarse de
    manera correcta.
    '''
    for reg in archivo:
        #Verificamos que el registro contenga unicamente 5 campos, caso contrario lanzamos un RuntimeError
        if(len(reg) != 5):
            raise RuntimeError("ERROR: Todos los registros deben contener 5 campos, ni mas ni menos.\nRegistro: [" + str(reg) + "]")

        #Verificamos que el campo 'CODIGO' no sea nulo, caso contrario lanzamos un RuntimeError
        if(reg['CODIGO'] == ''):
            raise RuntimeError("ERROR: El codigo no puede ser nulo.\nRegistro: [" + str(reg) + "]")

        #Verificamos que el campo 'CANTIDAD' sea un numero entero, caso contrario lanzamos un RuntimeError
        try:
            if(float(reg['CANTIDAD']) % 1 != 0):
                raise RuntimeError("ERROR: La cantidad debe ser un numero entero.\nRegistro: [" + str(reg) + "]")
        except ValueError:
            raise RuntimeError("ERROR: La cantidad debe ser un numero entero.\nRegistro: [" + str(reg) + "]")

        #Verificamos que el campo 'PRECIO' sea un numero decimal, caso contrario lanzamos un RuntimeError
        try:
            float(reg['PRECIO'])
        except ValueError:
            raise RuntimeError("ERROR: El precio debe ser un numero decimal.\nRegistro: [" + str(reg) + "]")

def obtener_clientes_con_nombre_incompleto(archivo, nombre_cliente_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de cliente
    incompleto, devuelve una lista con todos los nombres de clientes sin
    repetir (obtenidos de la columna CLIENTE del archivo) cuyo nombre
    contenga la cadena incompleta pasada por parámetro.
    '''
    #declaramos la variables con set para evitar duplicados
    clientes = set()
    #recorremos el archivo buscando los clientes que coincidan con el nombre de cliente incompleto.
    for reg in archivo:
        if(nombre_cliente_incompleto in reg['CLIENTE']):
            clientes.add(reg['CLIENTE'])
    return list(clientes)


def obtener_productos_con_nombre_incompleto(archivo, nombre_producto_incompleto):
    ''' Dado el contenido del archivo de datos y un nombre de producto
    incompleto, devuelve una lista con todos los nombres de productos sin
    repetir (obtenidos de la columna PRODUCTO del archivo) cuyo nombre
    contenga la cadena incompleta pasada por parámetro.
    '''
	#declaramos la variables con set para evitar duplicados
    productos = set()
	#recorremos el archivo buscando los productos que coincidan con el nombre de Producto incompleto.
    for reg in archivo:
        if(nombre_producto_incompleto in reg['PRODUCTO']):
            productos.add(reg['PRODUCTO'])
    return list(productos)


def obtener_productos_comprados_por_cliente(archivo, nombre_cliente):
    ''' Dado el contenido del archivo de datos y el nombre de un cliente,
    devuelve una lista de todos los nombres de productos comprados por
    el cliente, sin repetir.
    '''
    #recorro el archivo y busco los coincidentes y los agrego en lista de productos
    productos = set()
    for reg in archivo:
        if (nombre_cliente == reg['CLIENTE']):
            productos.add(reg['PRODUCTO'])
    return list(productos)


def obtener_clientes_de_producto(archivo, nombre_producto):
    ''' Dado el contenido del archivo de datos y el nombre de un producto,
    devuelve una lista de todos los compradores del producto, sin repetir.
    '''
    #recorro el archivo y busco los coincidentes y los agrego en lista de clientes
    clientes = set()
    for reg in archivo:
        if (nombre_producto == reg['PRODUCTO']):
            clientes.add(reg['CLIENTE'])
    return list(clientes)


def obtener_productos_mas_vendidos(archivo, cantidad_maxima_productos):
    ''' Devuelve una lista de tuplas de tamaño pasado por parámetro que
    representan los productos más vendidos, conteniendo como primer elemento
    el nombre del producto y como segundo elemento la cantidad de ventas.
    '''
    #Creamos un diccionario para guardar los productos como clave y la cantidad
    #de productos vendidos como valor.
    dic = dict()
    for reg in archivo:
        total = 0
        if(reg['PRODUCTO'] in dic):
            total = float(dic[reg['PRODUCTO']]) + float(reg['CANTIDAD'])
        else:
            total = float(reg['CANTIDAD'])

        dic[reg['PRODUCTO']] = str(total)

    #devuelve una tupla con los items del diccionario ordenados de mayor a menor
    prodcutos_ordenados = sorted(dic.items(), key = lambda element : (float(element[1]), element[0]), reverse=True)
    #Uso la funcion islice del modulo itertools para que devuelva los n primeros
    #registros de la tupla de productos ordenados.
    return itertools.islice(prodcutos_ordenados, 0, cantidad_maxima_productos)

def obtener_clientes_mas_gastadores(archivo, cantidad_maxima_clientes):
    ''' Devuelve una lista de tuplas de tamaño pasado por parámetro que
    representan los clientes que más gastaron, conteniendo como primer
    elemento el nombre del cliente y como segundo elemento el monto gastado.
    '''
	#Creamos un diccionario para guardar los clientes como clave y el monto 
    #total gastado como valor.
    dic = dict()
    for reg in archivo:
        total = 0
        if(reg['CLIENTE'] in dic):
            total = float(dic[reg['CLIENTE']]) + (float(reg['CANTIDAD']) * float(reg['PRECIO']))
        else:
            total = float(reg['CANTIDAD']) * float(reg['PRECIO'])

        dic[reg['CLIENTE']] = str(total)

	#devuelve una tupla con los items del diccionario ordenados de mayor a menor
    clientes_ordenados = sorted(dic.items(), key = lambda element : (float(element[1]), element[0]), reverse=True)
	#Uso la funcion islice del modulo itertools para que devuelva los n primeros
    #registros de la tupla de clientes ordenados.
    return itertools.islice(clientes_ordenados, 0, cantidad_maxima_clientes)
