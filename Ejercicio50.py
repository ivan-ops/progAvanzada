#Ejercicio 50
#Una función cuadrática univariada tiene la forma f (x) = ax2 + bx + c, donde a, byc son constantes, y a no es cero. 
#Las raíces de una función cuadrática se pueden encontrar al encontrar los valores de x que satisfacen
#la ecuación cuadrática ax2 + bx + c = 0. Una función cuadrática puede tener 0, 1 o 2 raíces reales. 
#Estas raíces se pueden calcular utilizando la fórmula cuadrática, que se muestra a continuación:
#root = (-b ± v b^2 - 4ac )/(2a)
#La parte de la expresión debajo del signo de raíz cuadrada se llama discriminante. 
#Si el discriminante es negativo, entonces la ecuación cuadrática no tiene raíces reales.
#Si el discriminante es 0, entonces la ecuación tiene una raíz real. 
#De lo contrario, la ecuación tiene dos raíces reales, y la expresión debe evaluarse dos veces, una vez usando un signo más, 
#y una vez usando un signo menos, al calcular el numerador.
#Escriba un programa que calcule las raíces reales de una función cuadrática. 
#Su programa debe comenzar solicitando al usuario los valores de a, byc. 
#Luego, debe mostrar un mensaje que indique el número de raíces reales, junto con los valores de las raíces reales (si las hay).

from math import sqrt

a = float(input("Inserta el valor para a: "))
b = float(input("Inserta el valor para b: "))
c = float(input("Inserta el valor para c: "))

discriminate = (b**2) - (4*a*c)

if discriminate < 0:
	print("Esta función cuadrática no tiene raíces reales.")
	
elif discriminate == 0:
	print("Esta función cuadrática tiene una raíz real.")
	
	root = -b / 2*a 
	
	print("Raiz real: {}".format(root))
	
elif discriminate > 0:
	print("Esta función cuadrática tiene dos raíces reales.")
	
	root1 = (-b + (sqrt(discriminate))) / (2*a)
	root2 = (-b - (sqrt(discriminate))) / (2*a) 
	
	print("Raices reales son: {} or {}".format(root1, root2))
