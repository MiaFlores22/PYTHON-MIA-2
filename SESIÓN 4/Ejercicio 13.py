""" Usando las propiedades de cadenas """
""" Concatenacion """

nombre = "Luke"
apellido = "Skywalker"

nombre_completo = "El nombre completo del usuario es: " + nombre + " " + apellido
print(nombre_completo)

""" Usando el formato format """

nombre_completo_2 = "El nombre completo del usuario es: {} {}".format(nombre,apellido)
print(nombre_completo_2)