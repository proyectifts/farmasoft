import interaccion_usuario
import consultas
import salida_resultados

NOMBRE_ARCHIVO_REGISTROS = "farmacia.csv"
CANT_MAX_RESULTADOS = 10


def obtener_opciones_menu_principal():
    ''' Devuelve una lista con todas las opciones que tiene el menú principal 
    del programa, en el orden que se mostrarán en pantalla.
    '''
    return ["Mostrar los n productos más vendidos", 
        "Mostrar los n clientes que más gastaron",
        "Mostrar los productos comprados por un cliente",
        "Mostrar los clientes que compraron un producto"]
    
    
def consultar_productos_mas_vendidos(archivo):
    ''' Función que exporta a un archivo de salida un listado de los productos 
    más vendidos, dado un archivo de entrada.
    Se le solicita al usuario la cantidad de productos que quiere listar.
    '''
    # Obtiene la cantidad a mostrar.
    print ("Ingrese la cantidad de productos a listar [1-{}].".format(CANT_MAX_RESULTADOS))
    cant_productos = interaccion_usuario.ingresar_numero(1, CANT_MAX_RESULTADOS)
    resultados = consultas.obtener_productos_mas_vendidos(archivo, cant_productos)
    
    # Exporta los resultados - se preparan los datos de acuerdo a la 
    #   documentación de la función del módulo salida_resultados.
    titulo_consulta = "%d productos más vendidos" % cant_productos
    cabecera = ("Producto", "Cantidad de ventas")
    nombre_salida = \
        salida_resultados.exportar_resultados(resultados, cabecera, titulo_consulta)
    
    print ("Resultados exportados al archivo " + nombre_salida)
    

def consultar_clientes_mas_gastadores(archivo):
    ''' Función que exporta a un archivo de salida un listado de los clientes 
    más gastadores, dado un archivo de entrada.
    Se le solicita al usuario la cantidad de clientes que quiere listar.
    '''
    # Obtiene la cantidad a mostrar.
    print ("Ingrese la cantidad de clientes a listar [1-{}].".format(CANT_MAX_RESULTADOS))
    cant_clientes = interaccion_usuario.ingresar_numero(1, CANT_MAX_RESULTADOS)
    resultados = consultas.obtener_clientes_mas_gastadores(archivo, cant_clientes)
    
    # Exporta los resultados - se preparan los datos de acuerdo a la 
    #   documentación de la función del módulo salida_resultados.
    titulo_consulta = "%d clientes más gastadores" % cant_clientes
    cabecera = ("Cliente", "Monto gastado")
    nombre_salida = \
        salida_resultados.exportar_resultados(resultados, cabecera, titulo_consulta)
    
    print ("Resultados exportados al archivo " + nombre_salida)
    

def consultar_productos_comprados_por_cliente(archivo):
    ''' Función que exporta a un archivo de salida un listado de los 
    productos comprados por un cliente, dado un archivo de entrada. 
    Se le solicita al usuario parte del nombre del cliente para después 
    seleccionar el nombre completo de una lista.
    '''
    # Obtiene el nombre del cliente.
    print ("Ingrese parte del nombre del cliente a consultar.")
    nombre_parcial = interaccion_usuario.ingresar_cadena_no_vacia()
    nombres_posibles = \
        consultas.obtener_clientes_con_nombre_incompleto(archivo, nombre_parcial)    
        
    if len(nombres_posibles) == 0:
        print ("No se encontraron productos con ese nombre.")
        return
    
    indice_nombre = \
        interaccion_usuario.mostrar_menu_generico(nombres_posibles, "Cancelar")
    if indice_nombre == -1:
        return
        
    nombre_cliente = nombres_posibles[indice_nombre]
    resultados = consultas.obtener_productos_comprados_por_cliente(archivo, nombre_cliente)
    
    # Exporta los resultados - se preparan los datos de acuerdo a la 
    #   documentación de la función del módulo salida_resultados.
    titulo_consulta = "Productos que compró el cliente %s" % nombre_cliente
    cabecera = ("Producto",)
    resultados = [ (resultado,) for resultado in resultados ]
    nombre_salida = \
        salida_resultados.exportar_resultados(resultados, cabecera, titulo_consulta)
    
    print ("Resultados exportados al archivo " + nombre_salida)
    

def consultar_clientes_de_producto(archivo):
    ''' Función que exporta a un archivo de salida un listado de los 
    clientes que compraron un producto, dado un archivo de entrada.
    Se le solicita al usuario parte del nombre del producto para después 
    seleccionar el nombre completo de una lista.
    '''
    # Obtiene el nombre del producto.
    print ("Ingrese parte del nombre del producto a consultar.")
    nombre_parcial = interaccion_usuario.ingresar_cadena_no_vacia()
    nombres_posibles = \
        consultas.obtener_productos_con_nombre_incompleto(archivo, nombre_parcial)
    
    if len(nombres_posibles) == 0:
        print ("No se encontraron productos con ese nombre.")
        return
    
    indice_nombre = interaccion_usuario.mostrar_menu_generico(nombres_posibles, "Cancelar")
    if indice_nombre == -1:
        return
        
    nombre_producto = nombres_posibles[indice_nombre]
    resultados = consultas.obtener_clientes_de_producto(archivo, nombre_producto)
    
    # Exporta los resultados - se preparan los datos de acuerdo a la 
    #   documentación de la función del módulo salida_resultados.
    titulo_consulta = "Clientes que compraron el producto %s" % nombre_producto
    cabecera = ("Cliente",)
    resultados = [ (resultado,) for resultado in resultados ]
    nombre_salida = \
        salida_resultados.exportar_resultados(resultados, cabecera, titulo_consulta)
    
    print ("Resultados exportados al archivo " + nombre_salida)
    
    
def consulta_ventas():
    ''' Inicia la interfaz con el usuario. Resuelve las consultas usando los
    métodos definidos en el módulo de consultas.
    '''
    print ("Bienvenido a FarmaSoft, el programa líder de consulta de ventas.")
    
    try:
        archivo = consultas.cargar_archivo(NOMBRE_ARCHIVO_REGISTROS)
    except RuntimeError as e:
        print (e)
        return
    
    seguir_consultando = True
    
    while seguir_consultando:
        print
        seleccion = interaccion_usuario.mostrar_menu_generico(
                obtener_opciones_menu_principal(), "Salir")
        
        if seleccion == 0:
            consultar_productos_mas_vendidos(archivo)
        elif seleccion == 1:
            consultar_clientes_mas_gastadores(archivo)
        elif seleccion == 2:
            consultar_productos_comprados_por_cliente(archivo)
        elif seleccion == 3: 
            consultar_clientes_de_producto(archivo)
        elif seleccion == -1:
            seguir_consultando = False
            
    print ("¡Gracias por usar FarmaSoft!")
        
        
consulta_ventas()
