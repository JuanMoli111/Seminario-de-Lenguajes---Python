#Un heterograma es una palabra cuyas letras no se repiten
#Ingresa la frase a determinar si es un heterograma
frase = input("Ingrese una frase")

#Crear el diccionario vacío
dicc = {}

for chars in frase:
    #Si el caracter no esta en el dicc, crea el key con apariciones = 1
    if not(char in dicc):
        dicc[char] = 1
        
    #Si el caracter está en el dicc, incrementa en 1 su cant de apariciones
    else:
        dicc[char] += 1

#decalarar el booleano
esHeterograma = True

#Recorrer el diccionario, si algun caracter (keys) tiene mas de una aparicion
#(values) significa que la frase no es heterograma
for key, value in dicc.items():
    if(value > 1):
        esHeterograma = False
        print("La frase o palabra, NO es heterograma")
        break

if(esHeterograma):
    print("La frase o palabra, es heterograma")

    
