""" Estructura de Datos """

""" Lista (count): Cantidad de veces que aparece un elemento que se repita en la lista """

lista = ["Python", "Ruby", "Java", "NodeJS", "TypeScript"]
lista.append("Python")
lista.append("Python")
lista.append("NodeJS")

print("Mi lista ACTUALIZADA es: {}".format(lista))
print("La cantidad de veces que se repite JAVA  es : {}".format(lista.count("Java")))
print("La cantidad de veces que se repite PYTHON  es : {}".format(lista.count("Python")))