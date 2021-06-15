#LOS METODOS DE CLASE SE DEFINIEN CON DECORADORES
#
class SuperHeroe():

    villanos = []


#SE NOTÓ CLS EN VEZ DE SELF POR QUE HACE REFERENCIA A LA CLASE, NO AL OBJETO DE UNA CLASE
    @classmethod
    def limpio_villanos(cls, confirmo= False):
        if confirmo:
            cls.villanos = []
        else:
            return cls.villanos

    def __init__(self,nombre,alias):
        self._nombre = nombre
        self._enemigos = []

SuperHeroe.limpio_villanos()

