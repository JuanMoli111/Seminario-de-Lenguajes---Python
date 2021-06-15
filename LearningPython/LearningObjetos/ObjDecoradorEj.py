#FUNCION DECORADOR
def deco(funcion):

    #DEFINE UNA FUNCION VARIABLE SEGUN QUE FUNCION SE LE PASE POR PARAMETRO
    def func_interna():
        print("Antes")
        funcion()
        print("Despues")

    #Decorador retorna la funcion interna
    return func_interna

""" Esto, con el @ deco es equivalente a:  """
@deco
def decimos_hola():
    print("Hola")
""" 
    esta linea de codigo:   
    
    saludo = decorador(decimos_hola)

"""

#Saludo le mando la funcion decimos hola, con esta, generó una funcion interna
#que retornó y almacenó en saludo, saludo es de tipo FUNCION
saludo = decorador(decimos_hola)