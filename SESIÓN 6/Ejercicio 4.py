
while True:
    try:
        x=int(input("Por favor ingresar un numero: "))
        break

    except ValueError:
        print("Ooops ! Este es un numero , intentar de nuevo")