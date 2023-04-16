""" REFORZAMIENTO # 2 - DICCIONARIO"""
" 3. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor de"
"salario en consola"

print()
diccionario = {"Nombre":"Mia Flores", "Edad": 21, "Salario":1500}
print("EL DICCIONARIO ES : {} ".format(diccionario))

diccionario["Dni"] = 70253695
print("EL NUEVO DICCIONARIO ES : {} ".format(diccionario))

del diccionario["Nombre"]
del diccionario["Edad"]
del diccionario["Dni"]
valor_salario = list(diccionario.values())
print("VALOR DE SALARIO EN CONSOLA: {}".format(valor_salario))

