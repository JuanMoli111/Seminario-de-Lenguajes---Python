

class A():
    def funcion1(self):
        return("Hola")

class B():
    def funcion1(self):
        return("Chau")

class C(A, B):
    def funcion1(self):
        return("Hasta la vista!")

    def saludo(self):
        #x = self.funcion1()
        x = super().funcion1()
        print(x)

obj = C()

obj.saludo()