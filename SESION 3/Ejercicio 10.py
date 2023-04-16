""" Estructura de Datos """

""" Obtener elementos de una lista: paises[i] """

paises = []
paises.append("Peru")
paises.append("Brasil")
paises.append("España")
paises.append("Canada")

print("Mi ista actual es: {}".format(paises))
print("El pais de mi lista con posicion 1 es: {}".format(paises[1]))
print("El pais de mi lista con posicion 1 es: {}".format(paises[3]))

edades = [34, 13, 13, 11, 13, 11, 14, 13]


print("El indice de mi edad erronea es: {}".format(edades[2]))

actualizar = edades[2] + 10
edades[2]= 27
edades[2] = edades[2] + 15
print("Mi lista ACTUALIZADA es: {}".format(edades))
