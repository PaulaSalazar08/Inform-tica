#Leer la primera palabra, deletrear, decir el n�mero de letras, de la segunda
#palabra lo mismo, y decir q palabra es m�s larga.

def palabra_mas_larga():
    palabra=raw_input("Introduce una palabra: ")
    longitud=len(palabra)
    print("La palabra "+palabra+" tiene "+str(longitud)+" letras")
    for cont in range(0,longitud):
        print(palabra[cont])



palabra_mas_larga()
