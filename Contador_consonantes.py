#Introduces una frase y el programa te cuenta
#1. Número de letras
#2. Número de consonantes
#3. Número de vocales
#4. Número de palabras
#5. Número de veces que aparece la letra o
#6. Encripta el mensaje sustituyendo cada letra por la siguiente en el abecedario

#1. Leo una cadena de caracteres con raw_input()

def contador():
    texto=raw_input("Dime algo bonito: ")#Leemos una cadena
    print("El texto tiene "+str(len(texto))+" caracteres")#Contamos el número de letras
    letra=""
    cont=0
    consonantes="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    nconsonantes=""
    for letra in texto[cont]:
        if letra in consonantes:
            nconsonantes=nconsonantes+1
        else:
            letra=letra+texto
        print("El texto tiene "+str(len(texto))+" consonantes")

contador()
