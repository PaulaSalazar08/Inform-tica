#Pide al usuario su nombre, apellido1 y apellido2 y el a�o de nacimiento
#Devuelve una contrase�a 3 primeras letras del nombre + 3 primeras letras
#de cada apellido + 2 �ltimas cifras del a�o de nacimiento
#EJEMPLO
#Paula Salazar Marin 2008
#contrase�a:PauSalMar08

def Password():
    Nombre=raw_input("Dime tu nombre: ") 
    Apellido1=raw_input("Dime tu primer apellido: ")
    Apellido2=raw_input("Dime tu segundo apellido: ")
    Fecha=raw_input("Dime tu a�o de nacimiento (aaaa): ")
    password=Nombre[0:3]+Apellido1[0:3]+Apellido2[0:3]+Fecha[2:4]
    print("Contrase�a: "+password)

Password()
