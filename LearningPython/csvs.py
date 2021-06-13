import csv

#EL ENCODING ES UN PARAMETRO IMPORTANTE, AL MENOS EN WINDOWS
arch = open("LearningPython/Datos/netflix_titles.csv","r",encoding = 'UTF-8')

##CSV.READER CREA EL READER, es un objeto que nos permite iterar estos tipos de archivos
##El delimiter le dice al reader cual es el caracter que separa los elementos
csvreader = csv.reader(arch, delimiter = ',')

##Guarda el encabezado, la primera linea del csv
header = csvreader.__next__()

""" Estas dos instrucciones son equivalentes:
header = next(csvreader)
header = csvreader.__next__()
"""
print(header)

##Informar algunos datos de manera comprensible, indicando a que tipo de dato corresponde cada columna
print("Titulo"+" "*15+"Director")

#Para cada linea del iterador de csvs
for linea in csvreader:
    #Si el show de netflix es argentino
    if linea[5] == "Argentina":

        #Imprime el titulo y el director
        print(f"{linea[2] : <40} {linea[3]}")


##Cierre el archivo
arch.close()