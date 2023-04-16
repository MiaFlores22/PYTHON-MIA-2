""" Manejo de Errores """
""" No se puede sumar con string """

def operaciones(a,b):
    try:
        resultado = a + b

    except TypeError:
        print("No es posible sumar entero con string")

    except ZeroDivisionError:
        print("No se puede dividir entre cero ")

    else:
        print(resultado)

operaciones(4, "Hola Pythonista")
operaciones(100,500)

