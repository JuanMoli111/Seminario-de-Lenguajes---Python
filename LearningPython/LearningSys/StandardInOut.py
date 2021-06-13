import sys

##Output a pantalla, mediante el archivo "salida estándar" (stdout) que se abre automáticamente en cualquier ejecucion
sys.stdout.write("Print de bajo nivel, esto ya parece assembler \n")

##Input desde teclado, mediante el archivo "entrada estándar" (stdin), que se abre automaticamente en cualquier ejecucion
nombre = sys.stdin.readline()

##Output del nombre registrado
sys.stdout.write(nombre)