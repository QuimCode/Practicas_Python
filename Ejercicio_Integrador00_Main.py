#----------------------------------------------------------------------------------------------------#

# Quimey Alejo Fontan - Programacion - DIV B - Giovanni

# Desafio Stark
# Industrias Stark es principalmente una empresa de defensa que desarrolla y fabrica
# armas avanzadas y tecnologías militares.

# Recientemente ha decidido ampliar su departamento de IT y para acceder a las
# entrevistas es necesario completar el siguiente desafío, el cual estará dividido en
# etapas. Cada semana recibiremos un nuevo pedido de parte de la empresa.

# La empresa compartió con todos los participantes cierta información confidencial
# de un grupo de superhéroes. Y semana a semana enviará una lista con los nuevos
# requerimientos. Quien supere todas las etapas accedera a una entrevista con el
# director para de la compañía.
# Set de datos

# La información a ser analizada se encuentra en el archivo data_stark.py, por tratarse
# de una lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera:

# from data_stark import lista_personajes

# Desafío #00:

# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener

#----------------------------------------------------------------------------------------------------#

from data_stark import lista_personajes

#----------------------------------------------------------------------------------------------------#

# B
print("Nombres de superhéroes:")
for personaje in lista_personajes:
    print(personaje["nombre"])

    #----------------------------------------------------------------------------------------------------#

# C
print("\nNombres y alturas de superhéroes:")
for personaje in lista_personajes:
    nombre = personaje['nombre']
    altura = int(float(personaje['altura'])) # Convertir altura a tipo entero
    print(f"{nombre} - Altura: {altura} cm")

    #----------------------------------------------------------------------------------------------------#

# D
max_altura = -1
max_personaje = None
for personaje in lista_personajes:
    altura = round(float(personaje["altura"])) # Convertir altura a tipo entero
    if altura > max_altura:
        max_altura = altura
        max_personaje = personaje["nombre"]
print(f"\nSuperhéroe más alto: {max_personaje} - Altura: {max_altura} cm")

    #----------------------------------------------------------------------------------------------------#

# E
min_altura = 999999
min_personaje = None
for personaje in lista_personajes:
    altura = round(float(personaje["altura"])) # Convertir altura a tipo entero
    if altura < min_altura:
        min_altura = altura
        min_personaje = personaje["nombre"]
print(f"\nSuperhéroe más bajo: {min_personaje} - Altura: {min_altura} cm")

    #----------------------------------------------------------------------------------------------------#

# F
total_altura = 0
for personaje in lista_personajes:
    total_altura += float(personaje["altura"])
print(f"La altura total de los superhéroes es de: {total_altura} cm")

    #----------------------------------------------------------------------------------------------------#

# G
print(f"\nSuperhéroe más alto: {max_personaje}")
print(f"Superhéroe más bajo: {min_personaje}")

    #----------------------------------------------------------------------------------------------------#

# H
max_peso = -1
max_personaje = None
min_peso = 999999
min_personaje = None
for personaje in lista_personajes:
    if float(personaje["peso"]) > max_peso:
        max_peso = float(personaje["peso"])
        max_personaje = personaje["nombre"]
    if float(personaje["peso"]) < min_peso:
        min_peso = float(personaje["peso"])
        min_personaje = personaje["nombre"]
print(f"\nSuperhéroe más pesado: {max_personaje} - Peso: {max_peso:.0f} kg")
print(f"Superhéroe menos pesado: {min_personaje} - Peso: {min_peso:.0f} kg")

    #----------------------------------------------------------------------------------------------------#  

# I
def imprimir_nombres():
    print("Nombres de superhéroes:")
    for personaje in lista_personajes:
        print(personaje["nombre"])

def imprimir_nombres_alturas():
    print("\nNombres y alturas de superhéroes:")
    for personaje in lista_personajes:
        nombre = personaje['nombre']
        altura = int(float(personaje['altura'])) # Convertir altura a tipo entero
        print(f"{nombre} - Altura: {altura} cm")

def imprimir_max_altura():
    max_altura = -1
    max_personaje = None
    for personaje in lista_personajes:
        altura = round(float(personaje["altura"])) # Convertir altura a tipo entero
        if altura > max_altura:
            max_altura = altura
            max_personaje = personaje["nombre"]
    print(f"\nSuperhéroe más alto: {max_personaje} - Altura: {max_altura} cm")

def imprimir_min_altura():
    min_altura = 999999
    min_personaje = None
    for personaje in lista_personajes:
        altura = round(float(personaje["altura"])) # Convertir altura a tipo entero
        if altura < min_altura:
            min_altura = altura
            min_personaje = personaje["nombre"]
    print(f"\nSuperhéroe más bajo: {min_personaje} - Altura: {min_altura} cm")

def imprimir_promedio_altura():
    total_altura = 0
    for personaje in lista_personajes:
        total_altura += float(personaje["altura"])
    promedio_altura = round(total_altura / len(lista_personajes))
    print(f"Altura promedio de los superhéroes: {promedio_altura} cm")

def imprimir_max_peso():
    max_peso = -1
    max_personaje = None
    for personaje in lista_personajes:
        if float(personaje["peso"]) > max_peso:
            max_peso = float(personaje["peso"])
            max_personaje = personaje["nombre"]
    print(f"\nSuperhéroe más pesado: {max_personaje} - Peso: {max_peso:.0f} kg")

def imprimir_min_peso():
    min_peso = 999999
    min_personaje = None
    for personaje in lista_personajes:
        if float(personaje["peso"]) < min_peso:
            min_peso = float(personaje["peso"])
            min_personaje = personaje["nombre"]
    print(f"\nSuperhéroe menos pesado: {min_personaje} - Peso: {min_peso:.0f} kg")

while True:
    opcion = input("\nIngrese el número de opción: \n1:Nombres - \n2:Nombres/Alturas - \n3:Altura Minima - \n4:Altura Maxima - \n5:Promedio Altura - \n6:Peso Maximo - \n7:Peso Minimo - \n0:Salir. ")
    if opcion == "1":
        imprimir_nombres()
    elif opcion == "2":
        imprimir_nombres_alturas()
    elif opcion == "3":
        imprimir_min_altura()
    elif opcion == "5":
        imprimir_promedio_altura()
    elif opcion == "6":
        imprimir_max_peso()
    elif opcion == "7":
        imprimir_min_peso()
    elif opcion == "4":
        imprimir_max_altura()
    elif opcion == "0":
        break

    #----------------------------------------------------------------------------------------------------#  
        #----------------------------------------------------------------------------------------------------#  
            #----------------------------------------------------------------------------------------------------#  
                #----------------------------------------------------------------------------------------------------#  
                    #----------------------------------------------------------------------------------------------------#  
                        #----------------------------------------------------------------------------------------------------#  