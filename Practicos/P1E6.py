#Funcion que dado un diccionario y un string, agrega el string como key
#y su cantidad de apariciones como value, si nunca aparecio agrega el elemento

def AgregarAparicion(dic,word):
    
    #Si la palabra no esta en el dicc, crea el key con apariciones = 1
    if not(word in dic):
        dic[word] = 1
        
    #Si la palabra está en el dicc, incrementa en 1 su cant de apariciones
    else:
        dic[word] += 1
        
    return dic



#String frase cualquiera
frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""

#Declara un diccionario vacio, declara un string vacio
dic = {}
word= ""

#Itera a traves de los caracteres de la frase
for car in frase:

    #Si el caracter no es espacio ni salto de linea, va concatenando una word
    if car != " " and car != '\n':
        word = word + car
    else:
        #Elimina simbolos de puntuacion de la palabra generada
        word.replace(',',"").replace('.',"")
        #Agrega la aparicion de esa palabra al diccionario
        AgregarAparicion(dic,word)
        #La palabra vuelve a estar en vacio
        word = ""
        
#Agrega la aparicion de esa palabra al diccionario    
AgregarAparicion(dic,word)

#Itera a traves de los keys del diccionario, imprime en minúsculas
#los key cuyo value sea igual a 1 (palabras con una unica aparicion)
for item in dic:
    if(dic[item] == 1):
        print(item.lower())
