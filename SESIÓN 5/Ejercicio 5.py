"""" Programacion funcional en Python """

var_1 = input("Ingresa el valor 1: ")
var_2 = input("Ingresa el valor 2: ")


"""" Imput : dos variables que pasaran por parametro de la funcion """
"""" a,b: parametros de la funcion restar"""

def resta(x,y):
    resultado = x - y
    return resultado

print("Resultado es  :{}".format(resta(int(var_1),int(var_2))))