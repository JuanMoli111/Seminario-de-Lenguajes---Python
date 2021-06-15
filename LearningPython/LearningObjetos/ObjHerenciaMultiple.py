##HERENCIA MULTIPLE, EL ORDEN EN QUE SE DEFINE LA HERENCIA MULTIPLE IMPORTA
##

class Jugador:

    def __init__(self, nom = "juan", equipo = None, tiene_equipo = False):
        self._nombre = nom
        self._equipo = equipo
        self._tiene_equipo = tiene_equipo

    def jugar(self):
        if(self._equipo != None):
            print(f"{self._nombre}   esta jugando en {self._equipo}")
        else:
            print(f"{self._nombre}   esta jugando solo")

class Deportista:

    def __init__(self, nom , equipo = None):
        self._nombre = nom
        self._equipo = equipo

    def jugar(self):
        print(f"mi equipo es    {self._equipo}")



class JugadorFifa(Jugador, Deportista):

    def __init__(self,nombre,equipo):
        Jugador.__init__(self,nombre,equipo,True)
        Deportista.__init__(self,nombre, equipo)

class JugadorLol(Deportista, Jugador):
    def __init__(self,nombre,equipo):
        Jugador.__init__(self,nombre,equipo,True)
        Deportista.__init__(self,nombre,equipo)



juan = JugadorFifa("Nico villa"," BARCA")

#Que pasa cuando llamo a .jugar()??  en este caso el jugador de fifa busca localmente el metodo .jugar, no lo encuentra,
#entonces busca el metodo en su primer clase base, en este caso jugador, lo encutra, lo ejecuta
juan.jugar()

pepe = JugadorLol("Pepe","RANKED")

#Que pasa cuando llamo a .jugar()??  en este caso el jugador de lol busca localmente el metodo .jugar, no lo encuentra,
#entonces busca el metodo en su primer clase base, en este caso Deportista, lo encuetra, lo ejecuta
pepe.jugar()

