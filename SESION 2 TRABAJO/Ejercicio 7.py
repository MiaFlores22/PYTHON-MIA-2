"""
                EJERCICIO 07
"""

""" De 3 números asignados (tú los propones) a 3 variables se pide hallar la suma de los 
valores de los módulos con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la 
suma.
"""

print()
num_1 = 44
num_2 = 37
num_3 = 152

suma = (num_1 % 3) + (num_2 % 5) + (num_3 % 7)
print("La suma de los valores de los módulos con 3, 5, y 7 respectivamente es : {}".format(suma))