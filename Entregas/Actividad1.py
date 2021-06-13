alumnos = '''
    "Agustin",
    "Alan",
    "Andrés",
    "Ariadna",
    "Bautista",
    "CAROLINA",
    "CESAR",
    "David",
    "Diego",
    "Dolores",
    "DYLAN",
    "ELIANA",
    "Emanuel",
    "Fabián",
    "Facundo",
    "Facundo",
    "FEDERICO",
    "FEDERICO",
    "GONZALO",
    "Gregorio",
    "Ignacio",
    "Jonathan",
    "Jonathan",
    "Jorge",
    "JOSE",
    "JUAN",
    "Juan",
    "Juan",
    "Julian",
    "Julieta",
    "LAUTARO",
    "Leonel",
    "LUIS",
    "Luis",
    "Marcos",
    "María",
    "MATEO",
    "Matias",
    "Nicolás",
    "NICOLÁS",
    "Noelia",
    "Pablo",
    "Priscila",
    "TOMAS",
    "Tomás",
    "Ulises",
    "Yanina",
    '''

eval1 = '''
 81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
 '''

eval2 = '''
 30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
 '''

def limpiar_strings(string):
    return string.replace("\"", "").replace(",", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace('"', "").replace("'", " ").split()


alumnos = limpiar_strings(alumnos)
eval1 = limpiar_strings(eval1)
eval2 = limpiar_strings(eval2)


calcular_notas_finales = list(map(lambda eval1, eval2: int(eval1)+int(eval2), eval1, eval2))


def opcion1():
    diccionario = {}

    for x in range(len(alumnos)):
        diccionario[alumnos[x]] = int(eval1[x]) + int(eval2[x])

    print(f'     Nombres           Eval1            Eval2            Sumas')

    for pos in range(len(alumnos)):
        print('%2s' % pos, ' ', alumnos[pos].ljust(11), '%8s' % eval1[pos], ' %15s' % eval2[pos], ' %16s ' % diccionario[alumnos[pos]])

    print('suma total de notas :', sum(calcular_notas_finales))
    print('promedio general de las notas', sum(calcular_notas_finales)/len(alumnos))

   

def opcion2():
    cond = int(input("""
Seleccione sobre que valores se realizará el reporte:

1)Eval1
2)Eval2
3)Suma de ambas notas
0)Salir

"""))

    if((cond != 0) and (cond in range(1,4))):
        valor1=int(input("ingrese el valor inferior del rango: "))
        valor2=int(input("ingrese el valor superior del rango: "))
        if(cond == 1):
            suma_notas=[(alumno,int(nota1)) for alumno,nota1 in zip(alumnos,eval1)]
            suma_notas= filter(lambda x: x[1]>=valor1 and x[1]<=valor2,suma_notas)
        elif(cond == 2):
            suma_notas=[(alumno,int(nota2)) for alumno,nota2 in zip(alumnos,eval2)]
            suma_notas= filter(lambda x: x[1]>=valor1 and x[1]<=valor2,suma_notas)
        elif(cond == 3):
            suma_notas=[(alumno,int(nota1)+int(nota2)) for alumno,nota1,nota2 in zip(alumnos,eval1,eval2)]
            suma_notas= filter(lambda x: x[1]>=valor1 and x[1]<=valor2,suma_notas)

        lista = list(suma_notas)       
        print('     Nombres           Notas')

        print('%2s ' % "Nombres".ljust(11), '%8s' % "Eval1", '%8s' % "Eval2", '%8s' % "Total")
        
        for i in range(len(lista)):
            print('%2s' % i, ' ', lista[i][0].ljust(11), '%8s' % lista[i][1])

def opcion3():
    opc=int(input("""
Seleccione el criterio de ordenamiento de los datos:

1)Nombre.
2)nota1.
3)nota2.
4)suma de ambas notas.
0)Salir

"""))
    if((opc != 0) and (opc in range(1,5))):
        lista=[(alumno.lower(),int(nota1),int(nota2),int(nota1)+int(nota2)) for alumno,nota1,nota2 in zip(alumnos,eval1,eval2)]  

        l=sorted(lista,key=lambda lista: lista[opc - 1])  

        print('     Nombre            nota1            nota2             suma notas')
        
        for pos in range(len(l)):
            print('%2s' % pos, ' ', str(l[pos][0]).ljust(11), '%8s' % str(l[pos][1]), ' %15s' % str(l[pos][2]), ' %16s ' % str(l[pos][3]))



def menu():
    cond = int(input("""
Seleccione una opcion del menu :
  1)Calcular el promedio de las notas finales de todxs lxs estudiantes.
   2)Realizar reporte
    3)Ordenar los datos, eligiendo un criterio
     0)Salir
"""))    
    while True:
        if(cond == 1):
            opcion1()    
        elif(cond == 2):
            opcion2()
        elif(cond == 3):
            opcion3()
            
        cond = int(input("""
Seleccione una opcion del menu :
  1)Calcular el promedio de las notas finales de todxs lxs estudiantes.
   2)Realizar reporte
    3)Ordenar los datos, eligiendo un criterio
     0)Salir
"""))   
       
        if(cond == 0):
            break

menu()
