alumnos = """
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
    """

eval1 = """
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
 """

eval2 = """
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
 """

alumnos = alumnos.replace('"',"").replace(',', "").split()

eval1 = eval1.replace(",", "").split()
eval2 = eval2.replace(",", "").split()

calcular_notas_finales = list(map(lambda eval1,eval2: int(eval1)+int(eval2),eval1,eval2))

diccionario = {}

for x in range(len(alumnos)):
    diccionario[alumnos[x]] = int(eval1[x]) + int(eval2[x])


def calcular_promedio(calcular_notas_finales):
    """esta funcion calcula el promedio de las notas finales"""

    return sum(calcular_notas_finales)/len(alumnos)


def opcion1 (calcular_notas_finales,calcular_promedio):
    diccionario= {}

    for x in range (len(alumnos)):
        diccionario[alumnos[x]]= int(eval1[x])+ int(eval2[x])

    print(f'     Nombres           Eval1            Eval2            Sumas')

    for pos in range(len(alumnos)):
        print('%2s' % pos,' ', alumnos[pos].ljust(11),'%8s'  % eval1[pos],' %15s' % eval2[pos],' %16s ' %  diccionario[alumnos[pos]])

    print('suma total de notas :',sum(calcular_notas_finales))
    print('promedio general de las notas', calcular_promedio(calcular_notas_finales))


def opcion2():

    opc = int(input("""Seleccione sobre qué valores se hara el reporte
        1) Eval1
        2) Eval2
        3) Suma
        """))
    
    while True:

        valInf = int(input("Ingrese el valor inferior del rango"))
        valSup = int(input("Ingrese el valor superior del rango"))
        
        if(opc == 1):
            suma_notas = [(alumno, int(nota1)) for alumno,nota1 in zip(alumnos,eval1)]
            suma_notas = filter(lambda x: x[1] >= valor1 and x[1] <= valor2,suma_notas)
            print(list(suma_notas))         
        elif(opc == 2):
            suma_notas = [(alumno, int(nota1)) for alumno,nota2 in zip(alumnos,eval2)]
            suma_notas = filter(lambda x: x[1] >= valor1 and x[1] <= valor2,suma_notas)
            print(list(suma_notas))
        elif(opc == 3):
            suma_notas = [(alumno, int(nota1) + int(nota2)) for alumno,nota1,nota2 in zip(alumnos,eval1,eval2)]
            suma_notas = filter(lambda x: x[1] >= valor1 and x[1] <= valor2,suma_notas)
            print(list(suma_notas))        
        if opc: 0
        break


def opcion3():
    opc = int(input("""Ordenar segun:
        1) Nombre
        2) notas1
        3) notas2
        4) suma notas
        """))

    lista = [(alumno.lower(), int(nota1), int(nota2), int(nota1) + int(nota2)) for alumno,nota1,nota2 in zip(alumnos,eval1,eval2)]

    
    while True:

        if(opc == 1):
            sorted(lista[0])    
        elif(opc == 2):
            sorted(lista[1])
        elif(opc == 3):
            sorted(lista[2])    
        elif(opc == 4):
            sorted(lista[3])

        print(lista)

        opc = int(input("""Ordenar segun:
        1) Nombre
        2) notas1
        3) notas2
        4) suma notas
        """))

        if opc: 0
        break
    
def menu():

    opc = int(input("""Seleccione una opcion
        0) Salir del menu
        1) Calcular el promedio de las notas finales de todos los estudiantes
        2) Realizar reportes
        3) Ordenar los datos
        """))
    
    while True:

        if(opc == 1):
            opcion1(calcular_notas_finales,calcular_promedio)
        elif(opc == 2):
            opcion2()
        elif(opc == 3):
            opcion3()    

        opc = int(input("""Seleccione una opcion
        0) Salir del menu
        1) Calcular el promedio de las notas finales de todos los estudiantes
        2) Realizar reportes
        3) Ordenar los datos
        """))

        if opc: 0
        break



menu()
