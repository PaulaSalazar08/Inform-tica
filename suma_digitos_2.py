#Escriba un programa que pida un número y devuelva la suma de sus dígitos. Por
#ejemplo, si introduce el 243 devuelve 9.

def suma_digitos_2():
    #Pedir un número y lo leo como un entero
    numero=input("Dime un número de varias cifras: ")
    suma=0
    permanecer=True #Mientras permanecer sea verdadero, el programa está atrapado en un bucle.
    while(permanecer==True):
        suma=suma+(numero%10) #suma acumula los restos
        numero=numero/10
        print("suma= "+str(suma)+"numero= "+str(numero))
        if(numero<10):
            suma=suma+numero #Sumo el último cociente
            permanecer=False
    print(suma)
        
suma_digitos_2()
