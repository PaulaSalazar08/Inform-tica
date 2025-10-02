#Ejercicio que lee una palabra y sustituye las vocales por 'u'
def ululador():
    frase_entrada=raw_input("Dime algo coherente: ")#Leo una palabra
    frase_salida="" #Creo una cadena vacía
    vocales="aeiou"
    vocales_mayusculas="AEIOU"
    for cont in range(0,len(frase_entrada)):
        if(frase_entrada[cont] in vocales):#Si la letra que toca es la 'a' ...
            frase_salida=frase_salida+'u'#...concateno una 'u'
        if(frase_entrada[cont] in vocales_mayusculas):
            frase_salida=frase_salida+'U'
        else:#Si no lo es
            frase_salida=frase_salida+frase_entrada[cont] #...concateno la letra
    print(frase_salida)

ululador()
