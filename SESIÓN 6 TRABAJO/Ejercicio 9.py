"""
REFORZAMIENTO 3
9. Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo-encapsulamiento) (sueldo superior a
4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto.
"""
class Persona():
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def Datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))

class Empleado(Persona):
    def __init__(self,sueldo):
        super().__init__()
        self.__sueldo = float(input("Ingrese sueldo: "))

    def Sueldo(self):
        super().Datos()
        print("Sueldo: {}".format(self.__sueldo))

    def impuestos (self):
        if self.__sueldo > 4000:
            print("DEBE PAGAR IMPUESTO")
            sueldo = self.__sueldo * 0.10
            print("El impuesto a pagar es de : {}".format(sueldo))
        else:
            print("NO PAGA IMPUESTO")

Empleado_1 = Empleado("")
print()
print("RESULTADO: ")
Empleado_1.Sueldo()
Empleado_1.impuestos()







