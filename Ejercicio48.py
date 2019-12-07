#Ejercicio 48
#El zodiaco chino asigna animales a a�os en un ciclo de 12 a�os.
#Un ciclo de 12 a�os se muestra en la tabla a continuaci�n. 
#El patr�n se repite a partir de ah�, con 2012 siendo otro a�o del drag�n, y 1999 siendo otro a�o de la liebre.

#Escriba un programa que lea un a�o del usuario y muestre el animal asociado con ese a�o. 
#Su programa deber�a funcionar correctamente durante cualquier a�o mayor o igual a cero, 
#no solo los que figuran en la tabla.

a�o = int(input("Inserte el a�o: "))

if a�o < 2000 or a�o > 2011:
	while a�o < 2000:
		a�o += 12 
	while a�o > 2011:
		a�o -= 12

if a�o == 2000:
	signo = "Dragon"
elif a�o == 2001:
	signo = "Serpinete"
elif a�o == 2002:
	signo = "Caballo"
elif a�o == 2003:
	signo = "Oveja"
elif a�o == 2004:
	signo = "Mono"
elif a�o == 2005:
	signo = "Gallo"
elif a�o == 2006:
	signo = "Perro"
elif a�o == 2007:
	signo = "Cerdo"
elif a�o == 2008:
	signo = "Rata"
elif a�o == 2009:
	signo = "Buey"
elif a�o == 2010:
	signo = "Tigre"
elif a�o == 2011:
	signo = "Liebre"
	
print("El animal asociado es: ",signo)
print("(according to Chinese Zodiac signs, of course...)")