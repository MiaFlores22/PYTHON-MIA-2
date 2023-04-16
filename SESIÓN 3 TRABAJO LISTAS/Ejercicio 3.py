""" REFORZAMIENTO # 2 """
" 3. Quita 2 elementos de tu nueva lista ítems por valor, no por índice. "

print()
print("LISTA: ")
items = ["Analisis y Diseño", "Logica", "Sistemas Operativos", "Fundamentos","Probabilidades", "Filosofia"]
items.append("Base_Datos")
items.append("Algoritmos Paralelos")
items.append("Circuitos Electricos")
items.append("Diseño de Sitemas")
print(items)

print()
print("LISTA ACTUALIZADA: ")
items.remove("Sistemas Operativos")
items.remove("Probabilidades")
print(items)
