#Ejercicio 48
#El zodiaco chino asigna animales a años en un ciclo de 12 años.
#Un ciclo de 12 años se muestra en la tabla a continuación. 
#El patrón se repite a partir de ahí, con 2012 siendo otro año del dragón, y 1999 siendo otro año de la liebre.

#Escriba un programa que lea un año del usuario y muestre el animal asociado con ese año. 
#Su programa debería funcionar correctamente durante cualquier año mayor o igual a cero, 
#no solo los que figuran en la tabla.

año = int(input("Inserte el año: "))

if año < 2000 or año > 2011:
	while año < 2000:
		año += 12 
	while año > 2011:
		año -= 12

if año == 2000:
	signo = "Dragon"
elif año == 2001:
	signo = "Serpinete"
elif año == 2002:
	signo = "Caballo"
elif año == 2003:
	signo = "Oveja"
elif año == 2004:
	signo = "Mono"
elif año == 2005:
	signo = "Gallo"
elif año == 2006:
	signo = "Perro"
elif año == 2007:
	signo = "Cerdo"
elif año == 2008:
	signo = "Rata"
elif año == 2009:
	signo = "Buey"
elif año == 2010:
	signo = "Tigre"
elif año == 2011:
	signo = "Liebre"
	
print("El animal asociado es: ",signo)
print("(according to Chinese Zodiac signs, of course...)")