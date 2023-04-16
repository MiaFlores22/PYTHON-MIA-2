
"""  Conversion de Datos """
"""  De string : str a enteros: int  """

var_1 = "700"
var_2 = 3500
var_3 = 40.56

#No se puede realizar la siguiente suma:
#   suma=var_1+var_2


""" Conversión """

conversion = int(var_1)
print("El valor de mi variable conversion es: {}".format(conversion))
print("El tipo de dato de mi variable conversion es: {}".format(type(conversion)))

suma = conversion + var_2
print("La suma de mis dos variables es: {}".format(suma))


""" Suma de dos variables int + float = float"""

suma_2 = var_2 + var_3
print("La suma de var_2 y var_3 es : {}".format(suma_2))


""" Conversión de flotante a entero """
conversion_2 = int(var_3)
print("El valor de mi variable conversion_2 es: {}".format(conversion_2))

