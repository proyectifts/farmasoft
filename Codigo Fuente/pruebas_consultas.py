import consultas

NOMBRE_ARCHIVO_VALIDO_1 = "./archivos_prueba/archivo_valido_1.csv"
NOMBRE_ARCHIVO_VALIDO_2 = "./archivos_prueba/archivo_valido_2.csv"
NOMBRE_ARCHIVO_VALIDO_3 = "./archivos_prueba/archivo_valido_3.csv"
NOMBRE_ARCHIVO_VALIDO_4 = "./archivos_prueba/archivo_valido_4.csv"

def correr_prueba(caso_prueba, descripcion, resultados_pruebas):
    ''' Comprueba la igualdad pasada por parámetro como caso_prueba y
    muesta la descripción y su resultado en pantalla.
    Si no se cumple la igualdad se suma uno a la clave correspondiente en el
    diccionario resultados_pruebas.
        caso_prueba es una igualdad a la que se le va a aplicar assert.
    descripcion es un texto descriptivo con el que se va a imprimir el
    resultado de la operación.
    resultados_pruebas es un diccionario con las claves "OK" y "ERROR", que
    identifican valores numéricos con la cantidad de pruebas pasadas y
    falladas, respectivamente.
    '''
    try:
        assert caso_prueba
        print ("Prueba %s: OK" % descripcion)
        resultados_pruebas["OK"] += 1
    except AssertionError:
        print ("Prueba %s: ERROR" % descripcion)
        resultados_pruebas["ERROR"] += 1


def prueba_obtener_productos_comprados_por_cliente(resultados_pruebas):
    archivo_1 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_1)

    descripcion = "compras de cliente válido C1 con configuración 1"
    res_esperado = ["P01", "P02", "P03"]
    res_real = consultas.obtener_productos_comprados_por_cliente(archivo_1, "C1")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "compras de cliente válido C2 con configuración 1"
    res_esperado = ["P01"]
    res_real = consultas.obtener_productos_comprados_por_cliente(archivo_1, "C2")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    descripcion = "compras de cliente inexistente C6 con configuración 1"
    res_esperado = []
    res_real = consultas.obtener_productos_comprados_por_cliente(archivo_1, "C6")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    archivo_2 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_2)

    descripcion = "compras de cliente válido C1 con configuración 2"
    res_esperado = ["P01", "P02", "P03"]
    res_real = consultas.obtener_productos_comprados_por_cliente(archivo_2, "C1")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "compras de cliente válido C2 con configuración 2"
    res_esperado = ["P01"]
    res_real = consultas.obtener_productos_comprados_por_cliente(archivo_2, "C2")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)


def prueba_obtener_clientes_de_producto(resultados_pruebas):
    archivo_1 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_1)

    descripcion = "clientes de producto válido P1 con configuración 1"
    res_esperado = ["C1", "C2", "C3", "C4"]
    res_real = consultas.obtener_clientes_de_producto(archivo_1, "P01")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "clientes de producto válido P2 con configuración 1"
    res_esperado = ["C1", "C5"]
    res_real = consultas.obtener_clientes_de_producto(archivo_1, "P02")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    archivo_2 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_2)

    descripcion = "clientes de producto válido P1 con configuración 2"
    res_esperado = ["C1", "C2", "C3", "C4"]
    res_real = consultas.obtener_clientes_de_producto(archivo_2, "P01")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "clientes de producto válido P2 con configuración 2"
    res_esperado = ["C1", "C5"]
    res_real = consultas.obtener_clientes_de_producto(archivo_2, "P02")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "clientes de producto inexistente P4 con configuración 2"
    res_esperado = []
    res_real = consultas.obtener_clientes_de_producto(archivo_2, "P04")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)


def prueba_obtener_nombres_posibles_de_clientes(resultados_pruebas):
    archivo_3 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_3)

    descripcion = "obtiene clientes cuando se especifica el nombre completo"
    res_esperado = ["C0"]
    res_real = consultas.obtener_clientes_con_nombre_incompleto(archivo_3, "C0")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    descripcion = "obtiene clientes sin repetir si hicieron varias compras"
    res_esperado = ["C1"]
    res_real = consultas.obtener_clientes_con_nombre_incompleto(archivo_3, "C1")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    descripcion = "obtener clientes diferencia espacios"
    res_esperado = ["C2"]
    res_real = consultas.obtener_clientes_con_nombre_incompleto(archivo_3, "C2")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    descripcion = "obtiene clientes cuando se especifica el nombre incompleto"
    res_esperado = ["CC3", "C3C", "DC3", "C3"]
    res_real = consultas.obtener_clientes_con_nombre_incompleto(archivo_3, "C3")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "obtiene clientes cuando sus nombres tienen espacios"
    res_esperado = ["C C4 C C"]
    res_real = consultas.obtener_clientes_con_nombre_incompleto(archivo_3, "C4")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)


def prueba_obtener_nombres_posibles_de_productos(resultados_pruebas):
    archivo_4 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_4)

    descripcion = "obtiene productos cuando se especifica el nombre completo"
    res_esperado = ["P0"]
    res_real = consultas.obtener_productos_con_nombre_incompleto(archivo_4, "P0")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    descripcion = "obtiene productos sin repetir si se compraron varios"
    res_esperado = ["P1"]
    res_real = consultas.obtener_productos_con_nombre_incompleto(archivo_4, "P1")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    descripcion = "obtener productos diferencia espacios"
    res_esperado = ["P2"]
    res_real = consultas.obtener_productos_con_nombre_incompleto(archivo_4, "P2")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)

    descripcion = "obtiene productos cuando se especifica el nombre incompleto"
    res_esperado = ["PP3", "P3P", "QP3", "P3"]
    res_real = consultas.obtener_productos_con_nombre_incompleto(archivo_4, "P3")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "obtiene productos cuando sus nombres tienen espacios"
    res_esperado = ["P P4 P P"]
    res_real = consultas.obtener_productos_con_nombre_incompleto(archivo_4, "P4")
    correr_prueba(res_esperado == res_real, descripcion, resultados_pruebas)


def prueba_obtener_productos_mas_vendidos(resultados_pruebas):
    archivo_1 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_1)

    descripcion = "2 productos mas vendidos con archivo 1"
    res_esperado = [("P01", "4.0"), ("P02", "2.0")]
    res_real = consultas.obtener_productos_mas_vendidos(archivo_1, 2)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    archivo_2 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_2)

    descripcion = "1 producto mas vendido con archivo 2"
    res_esperado = [("P01", "4.0")]
    res_real = consultas.obtener_productos_mas_vendidos(archivo_2, 1)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    archivo_3 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_3)

    descripcion = "3 productos mas vendidos con archivo 3"
    res_esperado = [("P1", "8.0"), ("P2", "2.0"), ("C1", "1.0")]
    res_real = consultas.obtener_productos_mas_vendidos(archivo_3, 3)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    archivo_4 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_4)

    descripcion = "2 productos mas vendidos con archivo 4"
    res_esperado = [("P1", "2.0"), ("QP3", "1.0")]
    res_real = consultas.obtener_productos_mas_vendidos(archivo_4, 2)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

def prueba_obtener_clientes_mas_gastadores(resultados_pruebas):
    archivo_1 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_1)

    descripcion = "2 clientes mas gastadores con archivo 1"
    res_esperado = [("C1", "3.0"), ("C5", "1.0")]
    res_real = consultas.obtener_clientes_mas_gastadores(archivo_1, 2)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    archivo_2 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_2)

    descripcion = "1 cliente mas gastador con archivo 2"
    res_esperado = [("C1", "3.0")]
    res_real = consultas.obtener_clientes_mas_gastadores(archivo_2, 1)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    archivo_3 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_3)

    descripcion = "3 clientes mas gastadores con archivo 3"
    res_esperado = [("C1", "2.0"), ("P1", "1.0"), ("DC3", "1.0")]
    res_real = consultas.obtener_clientes_mas_gastadores(archivo_3, 3)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    archivo_4 = consultas.cargar_archivo(NOMBRE_ARCHIVO_VALIDO_4)

    descripcion = "2 clientes mas gastadores con archivo 4"
    res_esperado = [("C1", "8.0"), ("C2", "2.0")]
    res_real = consultas.obtener_clientes_mas_gastadores(archivo_4, 2)
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)


def correr_pruebas():
    ''' Ejecuta las pruebas y muestra el resultado de toda la ejecución en
    pantalla.
    '''
    resultados_pruebas = { "OK" : 0, "ERROR" : 0 }

    prueba_obtener_productos_comprados_por_cliente(resultados_pruebas)
    prueba_obtener_clientes_de_producto(resultados_pruebas)
    prueba_obtener_nombres_posibles_de_clientes(resultados_pruebas)
    prueba_obtener_nombres_posibles_de_productos(resultados_pruebas)
    prueba_obtener_productos_mas_vendidos(resultados_pruebas)
    prueba_obtener_clientes_mas_gastadores(resultados_pruebas)

    print ("Pruebas corridas: %d OK, %d errores." % \
            (resultados_pruebas["OK"], resultados_pruebas["ERROR"]))


correr_pruebas()
