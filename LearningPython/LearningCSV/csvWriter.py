import csv
import os

#Creemos un csv
#Crea el archivo csv, los separadores con os funcionan tambien en linux
arch = open(f"LearningPython{os.sep}LearningCSV{os.sep}gastos.csv","r+")

#Crea el writer para csvs
writer = csv.writer(arch)

#Escribe la primer linea como encabezado
writer.writerow(["fecha", "monto"])

#Almacena diez gastos
for i in range(10):
    writer.writerow([f"{i}/06/21", i * 166])

arch.close()