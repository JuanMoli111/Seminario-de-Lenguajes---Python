import PySimpleGUI as sg


#Elementos de la interfaz, el layout es una lista de listas, 
#las listas internas funcionan en la interfaz, como grupos de elementos que aparecen a la misma altura
layout =[[sg.Text("INGRESA UN MONTO"),sg.InputText()],
        [sg.Text("INGRESA TIPO DE GASTO"),sg.InputText()],
        [sg.Button('OK'), sg.Button('Cancel')]]
            
#Creamos la ventana, cargando nuestro layout
window = sg.Window("Demostracion", layout, margins= (200,200))



#Iterar indefinidamente
while True:
    ##Leer los eventos y los valores de nuestra ventana en tiempo real
    ##Window.read() espera a la siguiente interaccion con un evento, entonces guarda los siguientes datos:

    #Event cargará el valor del evento con el que interactúe el usuario, en este ejmplo si apreta OK, event será un string 'OK'

    #Values es un diccionario, con tantos elementos como elementos de lectura de datos guarde el layout de la ventana
    #Las claves del diccionario enumeran los elementos de la ventana en el orden en que aparecen en la declaracion del layout
    #Los valores del diccionario guardarán el valor recibido por los elementos de la ventana
    #para este ejemplo, la clave 0 guardará el valor que se ingrese en el primer campo, y la clave 1 guardará el valor del segundo 
    event, values = window.read()

    print("Detecté un evento desde la ventana!")

    #Si el evento que se registró es cancel o salir, corta el loop
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break

    print(values)

    
#Salio del while mediante el break, debemos cerrar la ventana
window.close()
