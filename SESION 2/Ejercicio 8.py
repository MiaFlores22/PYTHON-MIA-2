"""  Conversion de Datos """

"""  De string : int a string: str  """

var_1 = 4000
var_2 = "Hello word"
var_3 = "500"

# No es posible lo siguiente:
# suma =  var_1 + var_3
# print(suma)

conversion = str(var_1)
print("El valor de mi variable conversion es : {}".format(conversion))
print("El valor de mi variable conversion es : {}".format(type(conversion)))


conversion_2 = int(var_3)
print("El valor de mi variable conversion_2 es : {}".format(conversion_2))
print("El valor de mi variable conversion_2 es : {}".format(type(conversion_2)))

suma = var_1 + conversion_2
print("El valor dela suma es : {}".format(suma))

suma_2 = var_2 + " " + var_3
print("El valor dela suma es : {}".format(suma_2))