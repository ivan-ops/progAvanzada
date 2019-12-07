#Ejercicio 57
#La mayor�a de los a�os tienen 365 d�as. Sin embargo, 
#el tiempo requerido para que la Tierra orbita alrededor del Sol es en realidad un poco m�s que eso. 
#Como resultado, se incluye un d�a adicional, el 29 de febrero, en algunos a�os para corregir esta diferencia. 
#Dichos a�os se denominan a�os bisiestos. Las reglas para determinar si un a�o es o no bisiesto son las siguientes:
#� Cualquier a�o que es divisible por 400 es un a�o bisiesto.
#� De los a�os restantes, cualquier a�o divisible por 100 no es bisiesto.
#� De los a�os restantes, cualquier a�o que sea divisible por 4 es un a�o bisiesto.
#� Todos los dem�s a�os no son bisiestos.
#Escriba un programa que lea un a�o del usuario y muestre un mensaje que indique si es o no un a�o bisiesto.

ano =  int(input("Introduce el a�o: "))

ano_bisi = False

if ano % 400 == 0:
	ano_bisi = True
elif ano % 100 == 0 and not ano % 400 == 0:
	ano_bisi = False 
elif ano % 4 == 0 and not ano % 100 == 0 and not ano % 400 == 0:
	ano_bisi = True 

if ano_bisi:
	print("Este es un a�o bisiesto")
else:
	print("Este no es un a�o bisiesto")