"""" Programacionmorientada a objetos con Python
    Clase y Metodos
"""


class Carro():
    """" Atributos """

    ruedas = 4

    """" Constructor: Valores que van a tener por defecto mi clase cuando se le instancia a una variable """

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """" Metodos: Son las funciones de la clase  """

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

"""" Instanciamos nuestra clase """
carro_1 = Carro("Azul", 90)
print("La velocidad inicial de mi carro es: {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.frena()
carro_1.frena()
print("La velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))