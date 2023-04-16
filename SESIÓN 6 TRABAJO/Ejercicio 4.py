"""
REFORZAMIENTO 3
4. Crea una función que al ingresar dos números por parámetro mostrará
todos los números que hay entre ellos (Usar la función una vez y
mostrar el resultado por consola). Los números serán ingresados por
consola por el usuario.
"""
class Numeros():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def numeros_intermedios(self):
        self.n1 = int(input("Inggresa el primer numero: "))
        self.n2 = int(input("Inggresa el segundo numero: "))
        print("Los numeros que hay entre {} y {} son: ".format(self.n1, self.n2))
        for i in range(self.n1 + 1,self.n2):
            print(i)

Numeros_1=Numeros("","")
Numeros_1.numeros_intermedios()



