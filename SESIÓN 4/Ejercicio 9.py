""" Uso del for """

ingenierias = ["Software", "Sistemas", "Industrial", "Quimica", "Mecanica"]

print("El tamaño de mi lista es: {}".format(len(ingenierias)))
print()
i = 1

for ingenieria in ingenierias:
    print(ingenieria)
    print("Esta es la vuelta numero: {}".format(i))
    i = i + 1
