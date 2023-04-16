""" Usando las propiedades de cadenas """

""" Requisitos:
- Ingresar tu nombre y apellido por consola (Con valor a una variable diferente) 
- Concatenar ambos valores en una sola variable
- Obtener el tamaño de tu nombre completo
- Imprimir el resultado final todo en mayuscula
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre_y_apellido = nombre + " " + apellido

print("Su nombre completo es: {}".format(nombre_y_apellido))
print("El tamaño es: {} ".format(len(nombre_y_apellido)))
print("NOMBRE EN MAYUSCULAS: {}".format(nombre_y_apellido.upper()))

"""
- Indicar mediante condicionales si el tamaño del nombre es 
"""
print()
if len(nombre) > len(apellido):
    print("El tamaño de nombre es mayor al apellido")
elif len(nombre) < len(apellido):
    print("El tamaño de apellido es mayor al nombre")
else:
    print("El tamaño del nombre es igual al del apellido")
