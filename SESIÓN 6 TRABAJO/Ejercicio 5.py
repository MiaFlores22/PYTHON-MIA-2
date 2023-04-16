"""
REFORZAMIENTO 3
5. Crear una clase llamada círculo que contenga radio (en el constructor),
y que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios
"""

class Circulo():
    def __init__(self,radio):
        self.radio = radio

    def Area(self,area_circulo):
        area_circulo = (3.1416*(radio**2))
        print("El area del circulo es: {}".format(area_circulo))

    def Perimetro(self,perimetro):
        perimetro = 2 * 3.1416 * radio
        print("El perimetro del circulo es: {}".format(perimetro))

Circulo_1 = Circulo("")
while True:
    try:
        print("Radio 1:")
        radio = int(input("Ingrese el radio 1: "))
        Circulo_1.Area(radio)
        Circulo_1.Perimetro(radio)
        break
    except ValueError:
        print("!Error!, el radio ingresado tiene que ser dato de tipo NUMERICO y ENTERO")


Circulo_2 = Circulo("")
while True:
    print("Radio 2:")
    try:
        radio = int(input("Ingrese el radio 2: "))
        Circulo_2.Area(radio)
        Circulo_2.Perimetro(radio)
        break
    except ValueError:
        print("!Error!, el radio ingresado tiene que ser dato de tipo NUMERICO Y ENTERO")

