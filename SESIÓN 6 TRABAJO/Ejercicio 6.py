"""
REFORZAMIENTO 3
6. Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, imprimirlos y un método para mostrar un mensaje con el
resultado de la nota y si ha aprobado (mayor o igual a 11) o no el alumno.
Instanciar la clase por lo menos 3 veces.
"""
class Alumno():
    def __init__(self,nombre,edad,nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def Mostrando_Datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Nota Final: {}".format(self.nota_final))

    def Resultado(self):
        if self.nota_final >= 11:
            print("Resultado final: APROBADO")
        else:
            print("Resultado final: DESAPROBADO")

Alumno_1 = Alumno("Rafael", 23, 18)
print("ALUMNO 1:")
Alumno_1.Mostrando_Datos()
Alumno_1.Resultado()
print()

Alumno_2 = Alumno("Monica", 21, 10)
print("ALUMNO 2:")
Alumno_2.Mostrando_Datos()
Alumno_2.Resultado()

print()
Alumno_3 = Alumno("Juan",29, 19)
print("ALUMNO 3:")
Alumno_3.Mostrando_Datos()
Alumno_3.Resultado()



