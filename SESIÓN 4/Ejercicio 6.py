""" Uso del uso condicional if  """

var1 = int(input("Ingrese su primer valor numerico: "))
var2 = int(input("Ingrese su segundo valor numerico: "))

if var1 > var2:
    print("El valor de var1 es mayor que el segundo valor ingresada")
elif var1 == var2:
    print("Los valores ingresados son iguales")
else:
    print("El valor de var1 no es mayor que la segunda variable")