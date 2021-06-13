cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los simbolos: @ y !):")

if len(cadena) > 10:
    print("Ingresaste mas de 10 caracteres")

if ("@" in cadena) or ("!" in cadena):
    print("Ingresaste alguno de estos simbolos: @ o !")
else:
    print("Ingreso OK")

