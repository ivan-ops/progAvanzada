#Ejercicio 50
#Una funci�n cuadr�tica univariada tiene la forma f (x) = ax2 + bx + c, donde a, byc son constantes, y a no es cero. 
#Las ra�ces de una funci�n cuadr�tica se pueden encontrar al encontrar los valores de x que satisfacen
#la ecuaci�n cuadr�tica ax2 + bx + c = 0. Una funci�n cuadr�tica puede tener 0, 1 o 2 ra�ces reales. 
#Estas ra�ces se pueden calcular utilizando la f�rmula cuadr�tica, que se muestra a continuaci�n:
#root = (-b � v b^2 - 4ac )/(2a)
#La parte de la expresi�n debajo del signo de ra�z cuadrada se llama discriminante. 
#Si el discriminante es negativo, entonces la ecuaci�n cuadr�tica no tiene ra�ces reales.
#Si el discriminante es 0, entonces la ecuaci�n tiene una ra�z real. 
#De lo contrario, la ecuaci�n tiene dos ra�ces reales, y la expresi�n debe evaluarse dos veces, una vez usando un signo m�s, 
#y una vez usando un signo menos, al calcular el numerador.
#Escriba un programa que calcule las ra�ces reales de una funci�n cuadr�tica. 
#Su programa debe comenzar solicitando al usuario los valores de a, byc. 
#Luego, debe mostrar un mensaje que indique el n�mero de ra�ces reales, junto con los valores de las ra�ces reales (si las hay).

from math import sqrt

a = float(input("Inserta el valor para a: "))
b = float(input("Inserta el valor para b: "))
c = float(input("Inserta el valor para c: "))

discriminate = (b**2) - (4*a*c)

if discriminate < 0:
	print("Esta funci�n cuadr�tica no tiene ra�ces reales.")
	
elif discriminate == 0:
	print("Esta funci�n cuadr�tica tiene una ra�z real.")
	
	root = -b / 2*a 
	
	print("Raiz real: {}".format(root))
	
elif discriminate > 0:
	print("Esta funci�n cuadr�tica tiene dos ra�ces reales.")
	
	root1 = (-b + (sqrt(discriminate))) / (2*a)
	root2 = (-b - (sqrt(discriminate))) / (2*a) 
	
	print("Raices reales son: {} or {}".format(root1, root2))
