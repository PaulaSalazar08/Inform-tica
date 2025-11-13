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
    print("Elige una opción (1-4): ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

def devuelve_suma(n1,n2):
    return(suma)
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    print(str(num1)+" + "+str(num2)+" = "+ str(num1+num2))

def devuelve_resta(n1,n2):
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    print(str(num1)+" - "+str(num2)+" = "+ str(num1-num2))

def devuelve_multiplicacion(n1,n2):
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    print(str(num1)+" * "+str(num2)+" = "+ str(num1*num2))

def devuelve_division(n1,n2):
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    print(str(num1)+" / "+str(num2)+" = "+ str(num1/num2))

def calculadora():
    #Lee dos números
    n1=raw_input("Introduce un número: ")
    n1=raw_input("Introduce otro número: ")
    #muestra el menú
    muestra_menu()
    #Lee la opción
    #invoca la función que hace lo que le hemos pedido
    opcion=input("Elige una opción (1-4): ")
    if(opcion==1):
        devuelve_suma(n1,2)
    if(opcion==2):
        devuelve_resta(n1,2)
    if(opcion==3):
        devuelve_multiplicacion(n1,2)
    if(opcion==4):
        evuelve_division(n1,2)


calculadora()
