#Haz un programa que lea una palabra y devuelva cuántas letras tiene,
#cuántas de ellas son vocales y cuantas son consonantes.
def cuenta_letras():
    palabra=raw_input("Introduce una palabra: ")
    longitud=len(palabra)
    print("La palabra "+palabra+" tiene "+str(longitud)+" letras")
    for cont in range(0,longitud):
        print(palabra[cont])

    
    
cuenta_letras()
