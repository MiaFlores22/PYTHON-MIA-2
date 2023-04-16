"""
REFORZAMIENTO 3

3. Crear una clase que contengo dos métodos, uno que pida ingresar un nombre y apellido,
un método para pedir su edad y otro método que lo imprima ambos resultados. Comprobar ambos
métodos instanciado la clase respectivamente
"""
class Datos():
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def ingresando_nombres_apellidos (self):
        self.nombre = str(input("Ingresa nombre: "))
        self.apellido = str(input("Ingresa apellido: "))

    def ingresando_edad (self):
        self.edad = int(input("Ingresa edad: "))

    def final_resultados(self):
        print(f"Nombres: {self.nombre}")
        print(f"Apellidos: {self.apellido}")
        print(f"Datos Completos: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")

Datos_1 = Datos("","","")
Datos_1.ingresando_nombres_apellidos()
Datos_1.ingresando_edad()
print()
print("RESULTADOS: ")
Datos_1.final_resultados()

