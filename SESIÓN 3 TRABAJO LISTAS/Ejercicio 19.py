""" REFORZAMIENTO # 2 """
" 19. Crea una lista vacía (con 10 posiciones), pide sus valores y devuelve la suma y la media de los números."

lista = []
suma = 0
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)
    suma = suma + numero
media = suma / 10
print()
print("LA LISTA CREADA ES: {}" .format(lista))
print("LA SUMA DE LOS NUMEROS ES: {}".format(suma))
print("LA MEDIA DE LOS NUMEROS ES: {}".format(media))