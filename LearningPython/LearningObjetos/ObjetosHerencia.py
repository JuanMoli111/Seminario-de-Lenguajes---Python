
class Jugador:

    def __init__(self, nom = "juan", equipo = None):
        self._nombre = nom
        self._equipo = equipo

    def jugar(self):
        if(self._equipo != None):
            print(f"{self._nombre}   esta jugando en equipo")
        else:
            print(f"{self._nomb re}   esta jugando solo")

class JugadorFifa(Jugador):

    def __init__(self,nombre,equipo):
        Jugador.__init__(self,nombre,equipo)


class JugadorLol(Jugador):
    def __init__(self,nombre,equipo):
        Jugador.__init__(self,nombre,"LOL")


juan = Jugador()
pepe = JugadorLol("Pepe","TEAM")

juan.jugar()
pepe.jugar()

print(pepe._nombre)