import PySimpleGUI as sg
#PYSIMPLEGUI es un framework para poder crear interfaces graficas de forma simple

#Que elementos podremos incluir en nuestras interfaces?
#sg.Popup:   una ventana  pequeña que aparece brevemente 
sg.Popup("Primer pop Up", button_color=('yellow','red',))

#Estos popups parecen retornar un string con el texto del boton que se oprime
#Por ejemplo, aqui un popup que nos da dos opciones YES o NO
print(sg.PopupYesNo("Desea enviar un yes o un no?",button_color=('green')))

#Otro ejemplo con el popup basico
print(sg.Popup("Presione Okay para imprimir OK en consola", button_color=('black','violet',)))

#Popup con opcion aceptar o cancelar
print(sg.PopupOKCancel("Okay o cancelar?"))

#Recibir un texto desde un popup
input_texto_desde_popup = sg.PopupGetText('Ingrese su nombre de usuario','Registro')

#Informar con popups, si el registro fue exitoso o no
if(input_texto_desde_popup != None and input_texto_desde_popup != ""):
    sg.Popup('Registro Exitoso','Te registraste exitosamente como ' + str(input_texto_desde_popup))
else:
    sg.Popup('ERROR','Error al registrarse, debe ingresar su nombre')


