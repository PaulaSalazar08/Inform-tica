#Introduces una frase y el programa te cuenta
#1. Número de letras
#2. Número de consonantes
#3. Número de vocales
#4. Número de palabras
#5. Número de veces que aparece la letra o
#6. Encripta el mensaje sustituyendo cada letra por la siguiente en el abecedario

def menu():
    #MENÚ
    print("Elige una opción (1-6): ")
    print("1. Contar el numero de letras")
    print("2. Contar el numero de consonantes")
    print("3. Contar el numero de vocales")
    print("4. Contar el numero de palabras")
    print("5. Contar el numero de veces que aparece la letra o")
    print("6. Encriptar el mensaje")

def contador_letras(texto):
    print("Tiene "+str(len(texto))+" caracteres")

def contar_consonantes(texto):
    n_consonantes=0
    vocales="aeiouAEIOU"
    numero="1234567890"
    for letra in texto:
        if(not((letra in vocales) or (letra==" ") or (letra in numero))):
            n_consonantes=n_consonantes+1
    print("Tiene "+str(n_consonantes)+ " consonantes")

def contar_vocales(texto):
    n_vocales=0
    vocales="aeiouAEIOU"
    numero="1234567890"
    for letra in texto:
        if(letra in vocales):
            n_vocales=n_vocales+1
    print("Tiene "+str(n_vocales)+ " vocales")

def contar_palabras(texto):   #def contar_palabras(texto):
    n_palabras=0              #n_palabras=0
    for letra in texto:       #longitud=len(texto.split())
        if(letra==" "):        #print("Hay "+str(longitud)+ " palabras")
            n_palabras=n_palabras+1
    print("Tiene "+str(n_palabras+1)+ " palabras")

def contar_oes(texto):
    n_oes=0
    for letra in texto:
        if(letra=='o' or letra=='O'):
            n_oes=n_oes+1
    print("Tiene "+str(n_oes)+ " oes")

def encriptar(texto):
    texto_encriptado=""
    for letra in texto:
        #print("letra= "+letra+" codigo= "+ str(ord(letra)))-> esto no funciona
        texto_encriptado=texto_encriptado+chr(ord(letra)+1)
    print("Texto encriptado: "+texto_encriptado)

def contador_total():
    #Pido el texto
    texto=raw_input("Introduce una frase: ")
    menu()
    opcion=input("Elige una opción (1-6): ")
    if(opcion==1):
        contar_letras(texto)
    if(opcion==2):
        contar_consonantes(texto)
    if(opcion==3):
        contar_vocales(texto)
    if(opcion==4):
        contar_palabras(texto)
    if(opcion==5):
        contar_oes(texto)
    if(opcion==6):
        encriptar(texto)


contador_total()
