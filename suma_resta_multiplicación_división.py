#Escribe un  programa que te pida dos números enteros.
#A continuación, muestra un menú por pantalla:
#1.  Sumar
#2. Restar
#3. Multiplicar
#4. Dividir
#¿Qué deseas hacer (1-4)?
#Dependiendo del número elegido, suma, resta, multiplica o divide los números y
#muestra por pantalla el resultado.
#En una segunda parte, el programa debe cuidar detalles como el hecho de evitar
#divisiones por cero. Si introduce un 0 como divisor, debe detectarlo y dar un
#mensaje de error. " DIVISIÓN ENTRE 0. Introduzca otros números" y volver a
#preguntar por la pareja de números.

def muestra_menu():
    print("*************************************************************")
    print("***                        MENÚ                           ***")
    print("*************************************************************")
    print("      |\      _,,,---,,")
    print("ZZZzz /,`.-'`'    -.  ;-;;,_")
    print("     |,4-  ) )-,_. ,\ (  `'-'")
    print("    '---''(_/--'  `-'\_)")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion=input("ELIJA UNA OPCIÓN (1-4): ")
    return(opcion)

def devuelve_suma(n1,n2):
    suma=n1+n2 #No se puede poner "respuesta" porque ya se ha puesto en otro lado del programa
    return(suma)

def devuelve_resta(n1,n2):
    resta=n1-n2
    return(resta)

def devuelve_multiplicacion(n1,n2):
    multiplicacion=n1*n2
    return(multiplicacion)

def devuelve_division(n1,n2):
    division=float(n1)/n2
    return(division)

def calculadora():
    #Lee dos números
    repetir=True
    while(repetir):
        n1=input("Introduce un número: ")
        n2=input("Introduce otro número: ")
        respuesta=0
        #muestra el menú y lee la opción
        opcion=muestra_menu()
        if(n2==0 and opcion==4):
            print("ERROR: vas a dividir para cero. Elige otros dos números.")
        else:
            repetir=False
    #invoca la función que hace lo que le hemos pedido
    if(opcion==1):
        respuesta=devuelve_suma(n1,n2)
    if(opcion==2):
        respuesta=devuelve_resta(n1,n2)
    if(opcion==3):
        respuesta=devuelve_multiplicacion(n1,n2)
    if(opcion==4):
        respuesta=devuelve_division(n1,n2)
    print("SOLUCIÓN: "+str(respuesta))

calculadora()
