

#X = 10

try:
    print(X)
except NameError:
    print("Se ejecuto el manejador de la excepcion NameError")
except:
    print("hubo un error desconocido")
else:
    print("No hubo un error")
finally:
    print("Esto se imprime siempre")