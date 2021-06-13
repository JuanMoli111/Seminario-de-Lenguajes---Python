import PySimpleGUI as sg


#El read devuelve los eventos que se producen en la ventana
#En este ejemplo los unicos eventos son cerrar y minimizar
#sg.Window(title="Hola Mundo!", layout= [[]], margins=(1000,550)).read()


#Layout es una lista de listas q contiene los elementos
#que puede tener la interfaz y la organiza 
layout = [[sg.Text("Hola Mundo!")], [sg.Button("OK")],
          [sg.Text('Ingresa un valor'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

#Window es la ventana, le damos el layout 'layout' creado antes y un tamaño
window = sg.Window("Primer Demo", layout, margins=(200,150))



while True:
    #READ LEE LOS EVENTO QUE ESTAN SUCEDIENDO
    
    event, values = window.read()

    #CHEQUEA LOS EVENTOS 
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break



window.close()

#Elementos
#Botones = file browse, folder browse, color chooser, date picker and +
# chechbox, radio button, listbox
# Slider, Progress bar
#
#Estilos: ChangeLookAndFeel
#
#
