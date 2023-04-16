from Funciones import suma, mutiplicar

var_1 = int(input("Ingrese su primer valor: "))
var_2 = int(input("Ingrese su segundo valor: "))

sum = suma(var_1,var_2)
print("El resultado de sus dos valores es: {}".format(sum))

mult = mutiplicar(var_1,var_2)
print("El resultado de sus dos valores es: {}".format(mult))
