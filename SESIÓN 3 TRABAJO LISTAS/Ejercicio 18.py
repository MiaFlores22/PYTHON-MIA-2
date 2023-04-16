""" REFORZAMIENTO # 2 """
"18. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes "
"repetidos (los cuales son impares dentro del rango indicado y que no sea el último impar)"
"   - Empezando desde 1 y no 0."
"   - Agregar un cadena en la posición 3 de la lista."
"   - Eliminar este valor string de la cadena usando del."

print()
lista = []
for i in range(1,30):
    if i % 2 != 0:
        lista.append(i)
print("LISTA CON LOS 15 PRIMEROS NUMEROS IMPARES: ")
print(lista)

print()
print("LISTA CON 3 NUMEROS FLOTANTES REPETIDOS: ")
for i in range(1,4):
    lista.append(3.28)
print(lista)

print()
print("LISTA CON CADENA EN LA POSICION 3: ")
lista.insert(2, "Buenos Días ")
print(lista)

print()
print("LISTA ELIMINANDO EL VALOR DE LA POSICION 3: ")
del lista[2]
print(lista)

