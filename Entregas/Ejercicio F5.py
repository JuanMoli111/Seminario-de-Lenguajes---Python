def completa_curso_de_10(cantidad, args):
	resp = input('Desea completar el curso? (S/N)  ')
	if resp.upper() == 'S':
		for cant in range (cantidad):
			nombre = input('Ingresa nombre de nuevo integrante')
			args = args + (nombre,)
	return args
 
curso1 = completa_curso_de_10(6,('Juan','Ana','Rocío','Estela'))
curso2 = completa_curso_de_10 (8,('Pablo', 'Pedro'))
 
print (f'El curso1 actualizado es: {curso1}')
print (f'El curso2 actualizado es: {curso2}')
        
