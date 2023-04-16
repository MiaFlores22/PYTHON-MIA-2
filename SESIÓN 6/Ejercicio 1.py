"""" POO en python """
"""" Encapsulamiento """

class A():
    def __init__(self):
        self.inicial = False
        self._contador = 0  #"Definiendo mi atributo privado"

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador

class B():
    """" Encapsulamiento """
    def __init__(self):
        self.inicial = True
        self.__contador = 0 #"Definiendo mi atributo privado"

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

varA = A()
varA.inicial = True
varA.incrementa()
varA.incrementa()

print("Resultado: {}".format(varA.cuenta()))
print("Contador A: {} ".format(varA._contador))
print("Valor de inicial A: {} ".format(varA.inicial))

print()
varB = B()
varA.inicial = False

varB.incrementa()
varB.incrementa()
varB.incrementa()
varB.incrementa()

print("Valor del contador B es : {}" .format(varB.cuenta()))
print("Valor de inicial B es : {}" .format(varB.inicial))

"""" No es posible invocar porque el encapsulamiento es fuerte """
print("{}".format(varB.__contador))


