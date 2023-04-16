from datetime import datetime, date

class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = "Peruana"

    def registrar(self):
        self.nombre=str(input("Ingresa Nombre: "))
        self.edad = int(input("Ingresa Edad: "))
        print("PERSONA REGISTRADA")
        tiempo = datetime.now()
        print("La fecha de su registro es: {}".format(tiempo))

    def cumpleanos(self):
        self.edad = self.edad + 1
        return self.edad



Persona_1 = Persona("Maria",12)
Persona_1.registrar()
Persona_1.cumpleanos()
print("Edad actualizada 2 veces es : {} anos".format(Persona_1.cumpleanos()))

