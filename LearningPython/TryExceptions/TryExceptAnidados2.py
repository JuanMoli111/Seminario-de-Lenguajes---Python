
dic = {0:"juan", 1: "diego", 2: "nico"}

y = 9

try:
    try:
        for x in range(0,6):
            print(dic[x])
        
    except KeyError:            #Va a levantar NameError xq 'z' no existe
        for x in range(0,6):
            print(dic[z])

    y = y + 1

    print(f"El valor de y es {y}")

except NameError:#                        <------------
    print("Variables que no existen!")


