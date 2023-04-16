"""" Programacion funcional en Python """

var_1 = 50
var_2 = 80

"""" Imput > dos variables que pasaran por parametro de la funcion """
"""" a,b: parametros de la funcion sumar """


def sumar(a, b):
    resultado = a + b
    return resultado


res = sumar(var_1,var_2)
"""" Output: Lo que retorna la funcion """
print(f"La suma es: {res}")
