""" REFORZAMIENTO # 2 """
" 12. Reconocer los tipos de cada dato en la lista creadas y mostrarla en consola (type())"
print()

print("LISTA CREADA 1: ")
lista_1 = [5, 16, 250, 22, 987, 36, 4, 0.23, 2.54]
print(lista_1)
print()

for i in range(len(lista_1)):
    print()
    print("La posicion es: {}".format(i))
    print("El tipo de dato es: {}".format(type(lista_1[i])))

print()
print("====================================")
print()

print("LISTA CREADA 2: ")
lista_2 = [2, False , 5.63 ,True, 6.23 ,True]
print(lista_2)
print()

for i in range(len(lista_2)):
    print()
    print("La posicion es: {}".format(i))
    print("El tipo de dato es: {}".format(type(lista_2[i])))