"""" Programacionmorientada a objetos con Python """

class Carro:
    """" Atributos """
    ruedas = 4
    """" Constructor: Valores que van a tener por defecto mi clase cuando se le instancia a una variable """

    def __init__(self,color,aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """" Metodos: Son las funciones de la clase  """

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena (self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad<0:
            velocidad = 0
        self.velocidad = velocidad

"""" Instanciamos nuestra clase """
carro_1 = Carro("Negro",50)
carro_2 = Carro("Rojo",30)
print("El color del primer carro es: {} ".format(carro_1.color))
print("La aceleracion de mi primer carro: {} ".format(carro_1.aceleracion))
print("La cantidad de ruedas de mi primer carro: {} ".format(carro_1.ruedas))
print()
print("El color de mi segundo carro: {} ".format(carro_2.color))
print("La aceleracion de mi segundo carro: {} ".format(carro_2.aceleracion))
print("La cantidad de ruedas de mi segundo carro: {} ".format(carro_2.ruedas))
