def decimos_hola(nombre):
    return f"Hola {nombre}"

def decimos_chau(nombre):
    return f"Chau {nombre}"


def saludo_juan(saludo):
    return saludo("Juan")


print(saludo_juan(decimos_chau))