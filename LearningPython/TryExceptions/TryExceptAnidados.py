

dic = {0:"juan", 1: "diego", 2: "nico"}

def funcion(dic, clave):
    try:
        print(dic[clave])
    except TypeError:
        print("Algo salio mal")


for i in range(3):
    try:
        funcion(dic,i)
    except KeyError:
        print("Error del tipo keyError sucediendo")