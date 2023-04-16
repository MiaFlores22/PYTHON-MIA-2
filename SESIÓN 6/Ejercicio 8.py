""" Manejo de Errores """

def operaciones(a, b):
    try:
        #resultado = a + b
        resultado = a / b
        return print(resultado)

    except (TypeError,ZeroDivisionError):
        print("Excepcion Zero Division Error/Type Error")

    else:
        print(resultado)

operaciones(4,10)
operaciones(4,0)
operaciones("Hola",100)

