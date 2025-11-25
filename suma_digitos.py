#Escriba un programa que pida un número y devuelva la suma de sus dígitos. Por
#ejemplo, si introduce el 243 devuelve 9.

def suma_digitos():
    #Pedir un número y lo leo como un entero
    numero=raw_input("Dime un número de varias cifras: ")
    longitud=len(numero)
    suma=0
    for cont in range(0,longitud):   #No se pone longitud+1 porque estamos en una cadena (raw_input), si estuviéramos en int (no es cadena) entonces sí que sería longitud+1
        suma=suma+int(numero[cont])
    #Trocearlo en cifras
    print(suma)
    #Sumo o acumulo las cifras en una variable acumuladora
        
suma_digitos()
