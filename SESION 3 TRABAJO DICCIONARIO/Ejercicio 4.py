""" REFORZAMIENTO # 2 - DICCIONARIO"""
"4. Elimina el key edad tipo de tu diccionario, incluyendo su valor"

print()
diccionario = {"Nombre":"Mia Flores", "Edad": 21, "Salario":1500}
print("EL DICCIONARIO ES : {} ".format(diccionario))

print()
del diccionario["Edad"]
print("DICCIONARIO ACTUALIZADO: {}".format(diccionario))