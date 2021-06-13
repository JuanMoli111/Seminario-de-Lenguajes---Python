NumPyText = """NumPy is the fundamental package needed for scientific computing with Python.

Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security
It provides:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities
Testing:

NumPy requires pytest. Tests can then be run after installation with:

python -c 'import numpy; numpy.test()'
Call for Contributions
The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good first issue" may be a good starting point. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

review pull requests
triage issues
develop tutorials, presentations, and other educational materials
maintain and improve our website
develop graphic design for our brand assets and promotional materials
translate website content
help with outreach and onboard new contributors
write grant proposals and help with other fundraising efforts
If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invite).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved."""


def ProcesarPalabras_CalcMax(word, d, Max, MaxWord):
    #Si la key (palabra) no se encuentra en el dicc, añadirla con contandor en 1 (es su primer aparicion)
    if not(word in d):
        d[word] = 1
            
    #Si la key se encuentra en el dicc, sumar 1 al contador de apariciones
    else:
        if(word in d):
            d[word] = d[word] + 1
            #Si el contador de esta palabra superó al maximo, actualizar max y MaxWord
        if d[word] > Max and MaxWord != word:
            Max = d[word]
            MaxWord = word
                
    print("Apariciones: " + str(d[word]) + ".   Palabra: " + word)   
        

    return d, Max, MaxWord



#Declara un string a vacio para almacenar las palabras
word = ""
#Declara un diccionario vacio para guardar la relacion palabras-apariciones
d = {}

Max = 0
MaxWord = ""

#Iterar a traves de cada caracter del README
for char in NumPyText:

    #concatena a con el caracter si es que existe.
    if char != " " and char != '\n':
        word = word + char
    #Si el caracter es espacio, ya se formo una palabra(procesamiento)
    else:
        #Procesar Palabras funcion
        d, Max, MaxWord = ProcesarPalabras_CalcMax(word,d,Max,MaxWord)
        #Vuelve a estar en blanco la variable palabra
        word = ""

#Procesar Palabras funcion
d, Max, MaxWord = ProcesarPalabras_CalcMax(word,d,Max,MaxWord)             
print("Apariciones: " + str(d[word]) + ".   Palabra: " + word)   
        
print(MaxWord)
    

    
    
