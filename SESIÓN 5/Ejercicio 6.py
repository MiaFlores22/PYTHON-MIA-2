var_1 = input("Ingresa el valor 1: ")
var_2 = input("Ingresa el valor 2: ")
var_3 = input("Ingresa el valor 3: ")


def media(x,y,z):
    resultado = (x+y+z)/3
    return resultado

print("La Media es :{}".format(media(int(var_1),int(var_2),int(var_3))))