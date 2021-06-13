def completa_curso_de_10(cantidad, args):
    print(f"el tipo de args*{type(args)}") 
    resp = input('Desea completar el curso? (S/N)')
    if resp.upper() == 'S':
        for cant in range (cantidad):
            nombre = input('Ingresa nombre de nuevo integrante')
            args = args + (nombre,)
    return args
 
curso1 = completa_curso_de_10(6,'Juan','Ana','Rocío','Estela' )
curso2 = completa_curso_de_10 (8, 'Pablo', 'Pedro')
 
print (f'El curso1 actualizado es: {curso1}')
print (f'El curso2 actualizado es: {curso2}')



#Error por *args que debe colocarse al final,

#al arreglarlo debe modificarse el llamado a las funciones, de lo contrario
#considerará el primer nombre como la variable cantidad, luego hace cualquier
#cosa ademas de no poder hacer el range del for

#si se envia args como lista, nos da error?
#que ventajas tiene enviarlo como lista? 
