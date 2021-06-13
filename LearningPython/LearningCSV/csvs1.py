#Una solucion equivalente a la del programa csvs.py

import csv

#Crea el objeto archivo, abre el archivo en lectura, codificacion UTF-88
arch = open("LearningPython/Datos/netflix_titles.csv","r",encoding = 'UTF-8')

##CSV.READER CREA EL READER iterador para estos tipos de archivos
##El delimiter por comas
csvreader = csv.reader(arch, delimiter = ',')

#Esta linea itera el csv, y crea una version filter solo con las lineas de las peliculas que sean argentinas
#Lambda: retornará aquellos x cuyo indice 5 sea 'Argentina' (creo)

#Filter, iterará y filtrará los elementos del csvreader, para los cuales el lambda retorne x (creo)
shows_argentinos = filter(lambda x: x[5] == 'Argentina', csvreader)

#Imprime los titulos y los directores en el filter de los shows argentinos
for elem in shows_argentinos:
    print(f"{elem[2]:<40} {elem[3]}")



arch.close()