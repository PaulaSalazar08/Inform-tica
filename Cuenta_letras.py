#Haz un programa que lea una palabra y devuelva cuántas letras tiene,
#cuántas de ellas son vocales y cuantas son consonantes.
def cuenta_letras():
    palabra=raw_input("Introduce una palabra: ")
    longitud=len(palabra)
    print("La palabra "+palabra+" tiene "+str(longitud)+" letras")
    print(palabra[0])
    print(palabra[1])
    print(palabra[2])
    print(palabra[3])

    
    
cuenta_letras()
