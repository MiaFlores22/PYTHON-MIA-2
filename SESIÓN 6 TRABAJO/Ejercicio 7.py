"""
REFORZAMIENTO 3
7. Crear una clase Persona con los siguientes requerimientos. La clase
tendrá como atributos el nombre y la edad de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor) y un método para mostrar los datos e indicar si la
persona es mayor de edad o no.
Instanciar por lo menos la clase con 2 diferentes personas.
"""
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def Mostrando_datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))

    def Resultado(self):
        if self.edad >= 18:
            print("Resultado: MAYOR DE EDAD")
        else:
            print("Resultado: MENOR DE EDAD")

Persona_1 = Persona("Carlos", 19)
print("PERSONA 1:")
Persona_1.Mostrando_datos()
Persona_1.Resultado()

print()
print("PERSONA 2:")
Persona_2 = Persona("Marta", 14)
Persona_2.Mostrando_datos()
Persona_2.Resultado()
