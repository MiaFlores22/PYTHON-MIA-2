""" Controlde Excepciones """
"""
TypeErrror
ZeroDivisionError ---> NO SE PUEDE DIVIDIR UN NUMERO ENTRO 0

OverFlowError --> Resultado de una operación aritmética es demasiado grande para ser representado.
                  Esto no puede ocurrir para los enteros

IndexError --> Indice de lista fuera de rango , cuando no exite un indice dentro de una lista

KeyError --> Eror de diccionario : Por ejemplo si hay un diccionario que tiene nombre, edad, dni y quieres extrar
            un key "ciudad" pero NO HAY 
            
FileNotFoundError ---> No existe el archivo en la ruta especificada

ImportError ---> Cuando estamos importando una libreria y NO EXISTE LA LIBRERIA
"""

""" Estructura y Uso """

""" 
    try: 
        Bloque de codigo 1
    except 'Excepcion_1':
        Bloque de codigo 2
    else:
        Bloque de codigo 3
"""

def operaciones(a, b):
    try:
        resultado = a/b

    except ZeroDivisionError:
        print("!No se puede dividir por cero!")
    else:
        print(resultado)

division(40, 0)
division(100, 50)
