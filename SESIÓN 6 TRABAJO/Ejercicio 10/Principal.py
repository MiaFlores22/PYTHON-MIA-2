"""
REFORZAMIENTO 3
10. Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)
"""

from Funciones import ingresar_nombre_apellido,seguro,Edad

nombre = str(input("Ingresa Nombre: "))
apellido = str(input("Ingresa Apellido: "))
datos = ingresar_nombre_apellido(nombre,apellido)

print()
edad = int(input("Ingresa edad: "))
Edades = Edad(edad)

print()
tipo_seguro = str(input("Ingresa Tipo de Seguro: "))
seg = seguro(tipo_seguro)