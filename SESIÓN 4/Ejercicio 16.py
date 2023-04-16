""" Usando las propiedades de cadenas """
""" Metodos Strings """

cadena = "Conexion a base de datos con Python"
cadena_2 = cadena.replace(cadena[0:6],"pppppp")
print("Cadena con reemplazos, tiene el siguiente valor actualizado {}".format(cadena_2))

""" Eliminando espacios en blanco de mi cadena (después) """

cadena_3 = "Conexion a base de datos con Python "
cadena_4 = cadena_3.rstrip()
print("Mi cadena con espacio en blanco eliminados es: {}".format(cadena_4))

""" Eliminando espacios en blanco de mi cadena (antes) """
cadena_5 = "               Conexion a base de datos con Python"
cadena_6 = cadena_5.lstrip()
print("Mi cadena con espacio en blanco eliminados es: {}".format(cadena_6))
