""" REFORZAMIENTO # 2 - DICCIONARIO"""
" 5. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene."

print()
diccionario = {"Nombre":"Mia Flores", "Edad": 21, "Salario":1500}
print("EL DICCIONARIO ES : {} ".format(diccionario))

print("DICCIONARIO CONVERTIDO EN LISTA:  {}".format(list(diccionario)))

valores = list(diccionario.values())
for i in range(len(valores)):
    print()
    print("El valor es: {}".format(valores[i]))
    print("El tipo de dato es: {}".format(type(valores[i])))