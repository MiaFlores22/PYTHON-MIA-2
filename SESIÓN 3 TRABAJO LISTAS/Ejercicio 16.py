""" REFORZAMIENTO # 2 """
" 16. Mostrar sólo los datos comprendidos entre la posición 10 y 35"

print()
lista = []
for i in range(1,101):
    lista.append(i)
print("LISTA CON LOS 100 PRIMEROS ENTEROS: ")
print(lista)

print()
for i in range(1,10):
    lista.remove(i)
for i in range(36,101):
    lista.remove(i)
print("LISTA CON LOS NUMEROS COMPRENDIDOS ENTRE 10 Y 35: ")
print(lista)