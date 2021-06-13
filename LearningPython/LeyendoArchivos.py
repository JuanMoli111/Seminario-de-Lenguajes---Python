import csv

archivo = open("netflix_titles.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')

#encabezado = csvreader.__next__()
encabezado = next(csvreader)
print(encabezado)

print("Titulo"+" "*35+"Director")


for linea in csvreader:

    if linea[1] == "TV Show" and linea[5] == "Argentina":
        print(f"{linea[2]:<40} {linea[3]}")


        
archivo.close()

