dicc = {('A','E','I','O','U','L','N','R','S','T'): 1,('D','G') : 2,('B','C','M','P') : 3, ('F','H','V','W','Y'): 4, ('K'): 5, ('J','X'): 8,('Q','Z'): 10}

word = input("Ingrese una palabra")

valor = 0

for char in word:

    for claves in dicc.keys():
        
        for i in range(len(claves)):

            if(char.upper() in claves):
                valor += dicc[claves]
                break;

print("Puntaje de la palabra es " + str(valor))

