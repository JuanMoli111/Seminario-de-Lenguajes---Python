##Getters y setters

class Demo:
    def __init__(self):
        self._x = 0


    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    #Por la forma dinamica de las definiciones de python, tambien pueden eliminarse las variables de instancia
    #Por esto pueden definirse ademas de setters y getters, los nuevos deletters

    def delx(self):
        del self._x

    #Definamos una propiedad, esto permite acceder a datos
    #privados a traves de los metodos definidos pero de una forma mas facil e intuitiva
    x = property(getx, setx, delx, "X es una propiedad")

obj = Demo()

obj.x = 20

print(obj.x)