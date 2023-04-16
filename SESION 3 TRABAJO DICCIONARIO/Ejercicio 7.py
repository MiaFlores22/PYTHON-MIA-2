""" REFORZAMIENTO # 2 - DICCIONARIO"""
" 7. Crear un diccionario con 6 departamentos en el país."
"    - Borrar cualquier departamento (uno) usando la palabra reservada del."
"    - Comprobar que no existe este departamento borrado dentro del diccionario."

print("TOTAL DE DEPARTAMENTOS: ")
departamentos = {"Departamento 1":"Chiclayo", "Departamento 2":"Lima", "Departamento 3":"Arequipa", "Departamento 4":"Ica", "Departamento 5":"Loreto","Departamento 6": "Cusco"}
print(departamentos)

print()
print("ELIMINANDO UN DEPARTAMENTO - LIMA")
del departamentos["Departamento 2"]
print(departamentos)
