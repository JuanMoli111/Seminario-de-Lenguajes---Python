#Definiendo y creando objetos en python
#Un objeto es una coleccion de datos con un comportaiento asociado en una unica entidad
#Un objeto tiene atributos y métodos, en python todo se maneja como objetos
#


class Jugador():

    #Propiedades, atributos de la clase, variables de instancia

    nombre = "juan"
    nick = "Impefacto"
    genero = "masculino"
    edad = 20
    puntos = 0

    ##Definir el constructor, podemos dar valores por defectos a los parametros de esta forma:
    def __init__(self, nom = "JuanxDefecto", nic = "Impe", genero = "Cyborg", edad = 20):
        self.nombre = nom
        self.nick = nic
        self.genero = genero
        self.edad = edad
        self.puntos = 0

    #Define un método
    #Los metodos siempre tienen un primer parametro que hace se asocia al objeto receptor,
    #en este caso se llama self pero es arbitrario
    def incrementar_puntos(self,puntos):
        self.puntos += puntos



#Crear jugador personalizado, mediante constructor
pepe = Jugador("Pepe","NickMoli","onvre",25)

#Crear a juan con constructor vacio, esto le asigna los valores por defecto del constructor
Juan = Jugador()


#Incrementa los puntos de Juan con el metodo
Juan.incrementar_puntos(200)

#Informa datos de los jugadores
print(str(Juan.edad) + "     " + str(Juan.puntos))

print(pepe.puntos)