""" Diccionarios en Python """

diccionario = {"nombre": "Alfredo", "edad": 28, "ciudad": "Lima"}

print("Mi diccionario actual es: {}.".format(diccionario))

""" Para eliminar valores de nuestros diccionarios usamos: del """

del diccionario["edad"]
print("Mi diccionario actualizado es: {}".format(diccionario))

del diccionario["nombre"]
print("Mi diccionario actualizado es: {}".format(diccionario))