"""
                EJERCICIO 11
"""

"""  Identificar que tipo de dato se obtiene al elevar un número a la exponente de 5 y 
luego dividirlo por 10. Mostrar el resultado en pantalla

"""
print()
numero = 47
resultado = (numero**5)/10

if resultado % numero == 0:
    resultado = int(resultado)
else:
    resultado = resultado

print("El tipo de dato que se obtiene del numero es {}: ". format(type(resultado)))