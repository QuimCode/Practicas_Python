#----------------------------------------------------------------------------------------------------#

# Quimey Alejo Fontan - Programacion - DIV B - Giovanni - MENU-01
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

#------------------------------------------------/EXPORTACIONES/----------------------------------------#

from data_stark import lista_personajes 
from Funciones01 import *

#---------------------------------------------------/MENU/--------------------------------------------#

while True:
    opcion = int(input("\n¿Qué dato desea obtener? \n"
                            "1. Nombre Masculinos \n"
                            "2. Nombre Femeninos \n"
                            "3. Altura Maxima Masculino \n"
                            "4. Altura Maxima Femenino \n"
                            "5. Altura Minima Masculino \n"
                            "6. Altura Minima Femenino \n"
                            "7. Promedio de Altura Masculino \n"
                            "8. Promedio de Altura Femenino \n"
                            "9. Nombre de la Altura Maxima Masculina \n"
                            "10. Nombres de las Alturas \n"
                            "11. Tipo de Ojos \n"
                            "12. Tipo de Pelo \n"
                            "13. Tipo de IQ \n"
                            "14. Lista Heroes Ojos \n"
                            "15. Lista Heroes Pelo \n"
                            "16. Lista Heroes IQ \n"
                            "17. Salir \n"
                            "Ingrese un numero por favor: "))

    match opcion:
            case 1:
                nombres_masculino()
            case 2:
                nombres_femenino()
            case 3:
                max_altura_masculino()
            case 4:
                max_altura_femenino()
            case 5:
                min_altura_masculino()
            case 6:
                min_altura_masculino()
            case 7:
                promedio_altura_masculino()
            case 8:
                promedio_altura_femenino()
            case 9:
                nombre_max_altura_masculino()
            case 10:
                informe_de_nombres()
            case 11:
                contar_heroes_ojos(lista_personajes)
            case 12:
                contar_heroes_pelo(lista_personajes)
            case 13:
                contar_heroes_iq(lista_personajes)
            case 14:
                listar_heroes_por_ojos(lista_personajes)
            case 15:
                listar_heroes_por_pelo(lista_personajes)
            case 16:
                listar_heroes_por_iq(lista_personajes)
            case 17:
                break