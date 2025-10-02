#Ejercicio que lee una palabra y sustituye las vocales por 'u'
def ululador():
    frase_entrada=raw_input("Dime algo coherente: ")#Leo una palabra
    frase_salida="" #Creo una cadena vacía
    for cont in range(0,len(frase_entrada)):
        if(frase_entrada[cont]=='a' or frase_entrada[cont]=='e' or frase_entrada[cont]=='i' or frase_entrada[cont]=='o'):
            frase_salida=frase_salida+'u'
        else:
            frase_salida=frase_salida+frase_entrada[cont]
    print(frase_salida)

ululador()
