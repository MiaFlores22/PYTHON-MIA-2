"""
REFORZAMIENTO 3

1. Escribir una clase en python que contenga un método que convierta un
número entero en su cubo.
"""
class Numero_Cubo():

    def __init__(self,numero):
        self.numero = numero

    def cubo(self,resultado):
        resultado = (numero**3)
        print("El cubo del numero {} es: {} ".format(numero, resultado))

objeto = Numero_Cubo("")
numero = int(input("Ingresa el numero: "))
objeto.cubo(numero)



