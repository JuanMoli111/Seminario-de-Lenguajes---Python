##PROPERTY CON HERENCIA, Aplicando ambos conceptos



class Demo:
    def __init__(self):
        self._x = 0


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

#Este ejemplo demuestra que se pueden heredar las property
#ya que son funciones setter y getter en este caso.

class Demo1(Demo):
    def __init__(self):
        super().__init__()

obj = Demo1()

obj.x = 10

print(obj.x)