class Demo:
    def __init__(self):
        self._x = 0

    ##Esto es equivalente al getter, mas intuitivo, facil, y 
    #permite usar las variables de instancia privadas sin problemas
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        print("estoy seteando")
        self._x = value

    @x.deleter
    def x(self):
        del self._x
 

obj = Demo()

obj.x = 10

print(obj.x)