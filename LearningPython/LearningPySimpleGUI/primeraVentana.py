import PySimpleGUI as sg

#Primera ventana simple en pysimplegui
##Podemos ver en los parametros 
#que el layout se inicializa como una lista con una lista vacia

#.read() devuelve los eventos que produce la ventana
#en este caso solo existe la cruz para cerrar la ventana 
sg.Window(title="Hola Mundo", layout=[[]], margins=(400,100)).read()



#Guardamos la ventana en una variable y hacemos el read aparte
window = sg.Window(title="Hola de nuevo", layout=[[]], margins=(100,100))

window.read()


#Hagamos el read en un bucle While infinito

while True:
    #Evente recibe los eventos de los elementos, values recibe los datos de los elementos 
    event, values = window.read()

    #Si apreta CLOSE que salga, 
    #SI NO CHEQUEAMOS ESTA CONDICION PYSIMPLEGUI DA ERROR CERRANDO LA VENTANA
    if event == sg.WIN_CLOSED :
        break



window.close()



