"""" Programacion funcional en Python """

def multiplica(a, b, c=1000):
    resultado = a*b*c
    return resultado


#Es correcta usar la funcion sin asignar un tercer valor

print("El resultado de mi funcion es: {}".format(multiplica(40,3)))


#Es correcta usar la funcion cambiando el valor del tercer parametro
print("El resultado de mi funcion es: {}".format(multiplica(40,3,10)))