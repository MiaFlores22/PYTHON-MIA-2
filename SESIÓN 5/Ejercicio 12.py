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


class CarroVolador(Carro):

    ruedas = 6

    def __int__(self, color, aceleracion, estado_volando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estado_volando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False

carro_1 = Carro("Rojo", 70)
carro_volador = CarroVolador("Blanco", 50)

print("Color de mi carro volador {}".format(carro_volador.color))
print("El estado inicial de mi carro volador {}".format(carro_volador.estadoVolando))

carro_volador.vuela()
carro_volador.acelerar()
carro_volador.acelerar()
print(carro_volador)