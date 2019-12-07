#Ejercicio 57
#La mayoría de los años tienen 365 días. Sin embargo, 
#el tiempo requerido para que la Tierra orbita alrededor del Sol es en realidad un poco más que eso. 
#Como resultado, se incluye un día adicional, el 29 de febrero, en algunos años para corregir esta diferencia. 
#Dichos años se denominan años bisiestos. Las reglas para determinar si un año es o no bisiesto son las siguientes:
#• Cualquier año que es divisible por 400 es un año bisiesto.
#• De los años restantes, cualquier año divisible por 100 no es bisiesto.
#• De los años restantes, cualquier año que sea divisible por 4 es un año bisiesto.
#• Todos los demás años no son bisiestos.
#Escriba un programa que lea un año del usuario y muestre un mensaje que indique si es o no un año bisiesto.

ano =  int(input("Introduce el año: "))

ano_bisi = False

if ano % 400 == 0:
	ano_bisi = True
elif ano % 100 == 0 and not ano % 400 == 0:
	ano_bisi = False 
elif ano % 4 == 0 and not ano % 100 == 0 and not ano % 400 == 0:
	ano_bisi = True 

if ano_bisi:
	print("Este es un año bisiesto")
else:
	print("Este no es un año bisiesto")