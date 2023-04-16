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
carro_1 = Carro("Blanco",40)

print("El color del primer carro es: {} ".format(carro_1.color))

carro_2 = Carro("Rojo",80)
carro_2.marchas = 30000

print("El numero de marchas de mi segundo carro es: {} ".format(carro_2.marchas))

"""" IMPORTANTE """
"""" No es posible llamar un atributo de dato que se le ha asignado a otra instancia de la clase """
#print("El numero de marchas de mi segundo carro es: {} ".format(carro_1.marchas))

