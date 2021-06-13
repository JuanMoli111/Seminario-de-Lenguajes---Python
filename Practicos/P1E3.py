#Declare un texto cualquiera
text = """Hace quince mil millones de años paso algo medio raro, no me acuerdo que
era por que yo no estaba pero me contaron que fue medio raro"""

#El usuario ingresa un caracter
char = input("Ingrese un caracter")

#Declarar un string vacio para almacenar temporalmente las palabras 
word = ""

#SI EL STRING CHAR TIENE 1 CARACTER DE LARGO, EL USUARIO CUMPLIO LO SOLICITADO
if (len(char) == 1):
    #Iterar a traves de cada caracter del texto
    for car in text:

        #concatena word con el caracter si es que existe.
        if car != " " and car != '\n':
            word = word + car
        #Si el caracter es espacio, ya se formo una palabra(procesamiento)
        else:

            if(word[0] == char):
                print(word)
            
            #Vuelve a estar en blanco la variable palabra
            word = ""   

#SI EL STRING TIENE MAS O MENOS DE UN CARACTER EL USUARIO NO CUMPLIO LO
#SOLICITADO Y DEBE INFORMARSE EL ERROR
else:
    print("ERROR; DEBE INGRESARSE UNO Y SOLO UN CARACTER")


    
