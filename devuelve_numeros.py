#Escribe un programa que pida un número y muestre por pantalla los tres números
#anteriores y los tres posteriores

def muestra_anteriores(numero,correlativo):
    for cont in range(1,correlativo+1):
        print(numero+cont)

def muestra_posteriores(numero,correlativo):
    for cont in range(1,correlativo+1):
        print(numero-cont)

def devuelve_numeros():
    #pedir un número
    numero=input("Dame un número: ")
    correlativo=input("Cuántos números anteriores y posteriores quieres: ")
    #mostrar por pantalla los tres números anteriores
    muestra_anteriores(numero,correlativo)
    #mostrar por pantalla los tres números posteriores
    muestra_posteriores(numero,correlativo)

devuelve_numeros()
