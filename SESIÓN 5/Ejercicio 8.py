
nombre = input("Ingresar nombre completo: ")

nom = nombre.split()

print(nom)
print(nom[3])
print("Sus apellidos son : {}".format(nom[len(nom)-2]) + " " + nom[len(nom)-1])
