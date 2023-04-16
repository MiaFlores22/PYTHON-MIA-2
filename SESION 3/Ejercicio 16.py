""" Diccionarios en Python """

varDiccionario = {"nombre": "Mysql", "tipo": "BDReelacional"}

""" Convirtiendo diccionario a lista """

list(varDiccionario)

print("Mi diccionario convertido es {}".format(list(varDiccionario)))

valores = list(varDiccionario.values())
print(valores)

keys = list(varDiccionario.keys())
print(keys)

lista_convertida = varDiccionario.items()
print(lista_convertida)


