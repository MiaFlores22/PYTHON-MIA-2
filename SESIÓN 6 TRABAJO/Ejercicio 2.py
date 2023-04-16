"""
REFORZAMIENTO 3

2. Crear una clase en python que contenga un método que revierta una cadena de palabras
    Input: "Hola Pythonista, seguimos adelante"
    Output: "adelante seghimos Pythonista Hola"
"""
class Revertir():
    def __init__(self,frase):
        self.frase = frase

    def revirtiendo(self,cadena):
        cadena = " ".join(reversed(frase.split()))
        print(f"La frase INVERTIDA es: {cadena}")

Revertir_1 = Revertir("")
frase = str(input("Ingresa la frase: "))
print("La frase ORIGINAL es: {}".format(frase))
Revertir_1.revirtiendo(frase)
