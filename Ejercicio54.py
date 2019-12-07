#Ejercicio 54
#La longitud de onda de la luz visible varía de 380 a 750 nanómetros (nm). 
#Si bien el espectro es continuo, a menudo se divide en 6 colores como se muestra a continuación:
#Escriba un programa que lea una longitud de onda del usuario e informe su color. 
#Muestre un mensaje de error apropiado si la longitud de onda ingresada por el usuario está fuera del espectro visible.

onda = int(input("Introduce un valor para una longitud de onda de luz visible en nanómetros: "))

color = ""

if onda >= 350 and onda < 450:
	color = "violet"
elif onda >= 450 and onda < 495:
	color = "blue"
elif onda >= 495 and onda < 570:
	color = "green"
elif onda >= 570 and onda < 590:
	color = "yellow"
elif onda >= 590 and onda < 620:
	color = "orange"
elif onda >= 620 and onda <= 750:
	color = "red"
	
if color != "":
	print("Esta longitud de onda tiene el color:  ",(color))
else:
	print("Esta longitud de onda está fuera del espectro de la luz visible.")