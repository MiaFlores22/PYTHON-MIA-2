""" Listas en Python """

""" listas: Recorrido de Listas """

sueldos = [1000, 3000, 6000, 8000, 9000, 12000]
print("El tamaño de mi lista es: {}".format(len(sueldos)))

for i in range(len(sueldos)):
    print("La posicion es: {}".format(i))
    print(sueldos[i])

print()
print("Mi lista ACTUALIZADA es: {}".format(sueldos))