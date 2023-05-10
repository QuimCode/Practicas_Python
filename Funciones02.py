#----------------------------------------------------------------------------------------------------#

# Quimey Alejo Fontan - Programacion - DIV B - Giovanni - FUNCIONES/DESAFIO-02
# Desafio Stark

#------------------------------------------------/EXPORTACIONES/----------------------------------------#

from data_stark import lista_personajes 

#------------------------------------------------/FUNCIONES-#02/---------------------------------------------#

def normalizador_datos_stark(una_lista):

    """
    DOCUMENTACION:: Función que recibe una lista de héroes y convierte al tipo de dato correcto solicitado en la consigna, 
    en este caso... serian las keys (solo con las keys que representan datos numéricos) y valida primero que el tipo de dato
    no sea del tipo al cual será casteado para evitar confusiones.

    PARAMETROS: lista_heroes (list): es la lista que va a tomar para normalizar los datos obtenidos y solicitados.

    RETORNO:  (list): Lista de héroes normalizada.
    """

    if not una_lista: # Compruebo si la lista esta vacia con el if not, y si lo esta retorno el resultado del print.
        print("Error: Lista de héroes vacía")
        return una_lista
    
    dato_modificado = False # Compruebo que el dato fue modificado a travez de una bandera.
    
    for heroe in una_lista:
        for key, value in heroe.items():
            if key in ["altura", "peso", "fuerza"]:
                if isinstance(value, str) and value.replace('.', '', 1).isdigit():
                    if "." in value:
                        heroe[key] = float(value)
                    else:
                        heroe[key] = int(value)
                    dato_modificado = True
    
    if dato_modificado:
        print("Datos normalizados")
    
    return una_lista

def obtener_nombre(heroe):

    """
    DOCUMENTACIÓN: Función que recibe un diccionario que representa a un héroe y devuelve una cadena de texto con el nombre del mismo.
    PARAMETROS: heroe (dict): Diccionario que representa a un héroe.
    RETORNO: (str): Cadena de texto con el nombre del héroe.
    """
    nombre = heroe.get("nombre")
    return f"Nombre: {nombre}"

def imprimir_dato(dato):

    """
    DOCUMENTACIÓN: Función que recibe un dato y lo imprime por consola.
    PARAMETROS: dato (any): Cualquier tipo de dato a imprimir.
    RETORNO: Nada.
    """

    print(dato)

def stark_imprimir_nombres_heroes(una_lista):

    """
    DOCUMENTACIÓN: Función que recibe un dato y lo imprime por consola.
    PARAMETROS: dato (any): Cualquier tipo de dato a imprimir.
    RETORNO: Nada.
    """

    if len(una_lista) == 0:
        print("La lista de heroes está vacía")
    else:
        for heroe in una_lista:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)

def obtener_nombre_y_dato(una_lista, nombre, altura):

    """
    DOCUMENTACIÓN: Función que recibe una lista de héroes y se encarga de imprimir por consola los nombres de cada uno.
    PARAMETROS: lista_personajes (list): Lista de diccionarios que representa a cada héroe.
    RETORNO: Nada.
    """
    
    for heroe in una_lista:
        if heroe["nombre"] == nombre:
            dato_altura = heroe.get(altura)
            if dato_altura is None:
                return "El héroe no tiene ese dato"
    return f"No se encontró un héroe con el nombre {nombre}"

def stark_imprimir_nombres_alturas(una_lista):

    """
    DOCUMENTACIÓN:  Función que recibe una lista de héroes y muestra en pantalla el nombre y la altura de aquellos héroes
    que tengan una altura definida. Si la lista está vacía, se retorna un valor de -1.
    PARAMETROS: lista_personajes (list): Lista de héroes a procesar.
    RETORNO: - Si la lista está vacía, se retorna un valor de -1. Si la lista no está vacía, se muestran en pantalla el nombre y la
    altura de los héroes que tengan una altura definida, pero no se retorna ningún valor.
    """
    

    if not una_lista:
        return -1
    for heroe in una_lista:
        altura = heroe.get("altura")
        if altura is not None:
            mensaje = f"Nombre: {heroe['nombre']} | Altura: {altura}"
            print(mensaje)

def calcular_max(una_lista, key):

    if not una_lista:
        return -1
    max_hero = None
    max_valor = 0
    primer_dato = True
    for hero in una_lista:
        valor = float(hero.get(key, 0))
        if primer_dato or valor > max_valor:
            max_hero = hero
            max_valor = valor
            primer_dato = False
    return max_hero, max_valor

def calcular_min(una_lista, key):

    if not una_lista:
        return -1
    min_hero = None
    min_valor = float('inf')
    primer_dato = True
    for hero in una_lista:
        valor = float(hero.get(key, float('inf')))
        if primer_dato or valor < min_valor:
            min_hero = hero
            min_valor = valor
            primer_dato = False
    return min_hero, min_valor

def calcular_max_min_dato(una_lista, tipo_calculo, key):

    if not una_lista:
        return "Lista vacía"
    if tipo_calculo == 'maximo':
        heroe, valor = calcular_max(una_lista, key)
    elif tipo_calculo == 'minimo':
        heroe, valor = calcular_min(una_lista, key)
    else:
        return "Tipo de cálculo no válido"
    return heroe, valor

def stark_calcular_imprimir_heroe(una_lista, tipo_calculo, key):

    heroe, valor = calcular_max_min_dato(una_lista, tipo_calculo, key)
    if isinstance(heroe, str):
        nombre = obtener_nombre(heroe)
        print(nombre)
    else:
        nombre = obtener_nombre(heroe)
        if tipo_calculo == 'maximo':
            mensaje = f"Mayor {key.capitalize()}: {nombre} | {key}: {valor}"
        else:
            mensaje = f"Menor {key.capitalize()}: {nombre} | {key}: {valor}"
        print(mensaje)

def sumar_dato_heroe(una_lista, key):

    suma = 0
    for heroe in una_lista:
        if isinstance(heroe, dict) and heroe != {} and key in heroe:
            suma += float(heroe[key])
    return suma

def dividir(dividendo, divisor):

    if divisor == 0:
        return 0
    else:
        return dividendo / divisor

def calcular_promedio(una_lista, key):

    suma = sumar_dato_heroe(una_lista, key)
    cantidad_heroes = len(una_lista)
    if cantidad_heroes == 0:
        return 0
    else:
        promedio = dividir(suma, cantidad_heroes)
        return promedio
    
def stark_calcular_imprimir_promedio_altura(heroe):

    if len(heroe) == 0:
        return -1
    else:
        altura_promedio = calcular_promedio(heroe, 'altura')
        if altura_promedio == -1:
            return -1
        else:
            mensaje = f"Altura promedio: {altura_promedio}"
            print(mensaje)

def imprimir_menu(una_lista):
    while True:
        opcion = int(input("\n¿Qué dato desea obtener? \n"
                                "1. Convertidor de Datos \n"
                                "2. Nombre de Heroes \n"
                                "3. Imprimir Nombres/Alturas \n"
                                "4. Imprimir Maximos/Minimos \n"
                                "5. Imprimir Promedio de Altura \n"
                                "6. Imprimir Menu Alternativo \n"
                                "7. Salir \n"
                                "Ingrese un numero por favor: "))

        match opcion:
                case 1:
                    normalizador_datos_stark(una_lista)
                case 2:
                    stark_imprimir_nombres_heroes(una_lista)
                case 3:
                    stark_imprimir_nombres_alturas(una_lista)
                case 4:
                    stark_calcular_imprimir_heroe(una_lista, 'maximo', 'altura')
                    stark_calcular_imprimir_heroe(una_lista, 'minimo', 'altura')
                case 5:
                    stark_calcular_imprimir_promedio_altura(una_lista)
                case 6:
                    stark_marvel_app(una_lista)
                case 7:
                    break
    print(opcion)


def validar_entero(numero_string):
    return numero_string.isdigit()


def stark_menu_principal():
    opcion_valida = False
    while not opcion_valida:
        imprimir_menu()
        opcion = input("Ingrese una opción: ")
        if validar_entero(opcion) and 1 <= int(opcion) <= 6:
            opcion_valida = True
            return int(opcion)
        else:
            print("La opción ingresada no es válida. Intente nuevamente.\n")
    return -1

def stark_marvel_app(una_lista):
    while True:
        print("Seleccione una opción:")
        print("1. Calcular y mostrar la maxima altura.")
        print("2. Calcular y mostrar la minima altura.")
        print("3. Calcular y mostrar el maximo peso.")
        print("4. Calcular y mostrar el minimo peso.")
        print("5. Calcular y mostrar la maxima edad.")
        print("6. Calcular y mostrar la maxima edad.")
        print("7. Salir.")
        opcion = input("Opción: ")
        
        if opcion == "1":
            stark_calcular_imprimir_heroe(una_lista, 'maximo', 'altura')
        elif opcion == "2":
            stark_calcular_imprimir_heroe(una_lista, 'minimo', 'altura')
        elif opcion == "3":
            stark_calcular_imprimir_heroe(una_lista, 'maximo', 'peso')
        elif opcion == "4":
            stark_calcular_imprimir_heroe(una_lista, 'minimo', 'peso')
        elif opcion == "5":
            stark_calcular_imprimir_heroe(una_lista, 'maximo', 'fuerza')
        elif opcion == "6":
            stark_calcular_imprimir_heroe(una_lista, 'minimo', 'fuerza')
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Intente de nuevo.")