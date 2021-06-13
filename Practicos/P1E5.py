frase = input("Ingrese una frase: ").lower()

cadena = input("Ingrese un string: ").lower()

cant = 0
word = ""

#Iterar a traves de cada caracter del texto
for car in frase:

    #concatena word con el caracter si es que existe.
    if car != " " and car != '\n':
        word = word + car
    #Si el caracter es espacio, ya se formo una palabra(procesamiento)
    else:
        
        if(cadena.lower() == word.lower()):
            cant = cant + 1
            
        #Vuelve a estar en blanco la variable palabra
        word = ""

        
if(cadena.lower() == word.lower()):
    cant = cant + 1
            
print(cant)

