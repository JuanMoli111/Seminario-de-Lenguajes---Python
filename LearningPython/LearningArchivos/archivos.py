#Escritura en un archivo binario

#Abrimos el archivo, pasando la ruta y el modo de apertura, esto crea un objeto archivo para pytohn en arch
arch = open("LearningPython/LearningArchivos/gastos","rb+")

#Escribir en el archivo,    bytes convierte el string a binario, necesita un formato de codificacion-decodificacion
arch.append(bytes(f"done\"",'UTF-8'))


arch.close()