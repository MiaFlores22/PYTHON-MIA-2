""" REFORZAMIENTO 3:
8. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono y el email. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto
"""
class Agenda():
    def __init__(self):
        self.contactos = []

    def menu(self):
        f = 1
        while f == 1:
            menu = """
            Agenda Personal:
            1. Añadir Contacto
            2. Muestra de contactos
            3. Buscar contacto
            4. Cerrar agenda
            """
            print(menu)
            opcion = int(input("Introduzca la opción deseada: "))
            print()
            if opcion == 1:
                self.anadir()
            elif opcion == 2:
                self.muestra()
            elif opcion == 3:
                self.buscar()
            elif opcion == 4:
                print("Saliendo  ...")
                exit()

            f = int(input("DESEA SEGUIR? 1--> SI, 2---> NO: "))

    def anadir(self):
        print("==========================")
        print("Añadiendo nuevo contacto")
        nom = input("- Ingrese nombre: ")
        telf = int(input("- Ingrese teléfono: "))
        email = input("- Ingrese email: ")
        self.contactos.append({'nombre': nom, 'telf': telf, 'email': email})

    def muestra(self):
        print("=====================")
        print("LISTA DE CONTACTOS: ")
        if len(self.contactos) == 0:
            print("No hay ningún contacto en la agenda")
        else:
            for x in range(len(self.contactos)):
                print(self.contactos[x]['nombre'])
        print("=====================")

    def buscar(self):
        print("=====================")
        print("Buscador de contactos: ")
        nom = input("- Introduzca el nombre del contacto: ")
        for x in range(len(self.contactos)):
            if nom == self.contactos[x]['nombre']:
                print("Datos del contacto: ")
                print("- Nombre: ", self.contactos[x]['nombre'])
                print("- Teléfono: ", self.contactos[x]['telf'])
                print("- E-mail: ", self.contactos[x]['email'])
                return x
            print("=====================")

Agenda_1 = Agenda()
Agenda_1.menu()
print()