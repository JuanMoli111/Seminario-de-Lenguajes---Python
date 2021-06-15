#Se pueden definir metodos "especiales" en los objetos de python
#Por ejemplo un metodo nombrado __init__ será para python, el constructor a ejecutar al instanciar de esta clase
#Un metodo nombrado __str__ será el metodo a ejecutar al realizar print(OBJECT)

#De la misma forma pueden definirse para operadores, comparadores e instrucciones, permitiendo definir 
#la forma en que se realizan en objetos, por ejemplo pudiendo comparar que objeto es menor o mayor, si son iguales
#entre otras cosas interesantes

class Jugador:

    ##Metodo constructor
    def __init__(self, nom = "juan"):
        self._nombre = nom


    ##Metodo string, informa el nombre del jugador
    def __str__(self):
        return (f"{self._nombre}  es un jugador")


    ##Metodo equals, retorna true o false segun sean iguales o no, los atributos a comparar
    def __eq__ (self, otro):
        return (self._nombre == otro._nombre)


juan = Jugador()
pepe = Jugador("Pepe")

print(juan == pepe)