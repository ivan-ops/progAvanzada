#Ejercicio 52
#En el ejercicio anterior, creó un programa que convierte una calificación de letra en el número equivalente de puntos de calificación. 
#En este ejercicio creará un programa que invierte el proceso y convierte de un valor de calificación ingresado 
#por el usuario a una calificación de letra. Asegúrese de que su programa maneje los valores de calificación que se encuentran 
#entre las calificaciones de las letras. 
#Estos deben redondearse al grado de letra más cercano. 
#Su programa debe reportar A + para un promedio de calificaciones de 4.0 (o más).

puntos = float(input("Inserte la califiacion en puntos: "))

grado = ""

if puntos >= 0 and puntos < 0.5:
	grado = "F"
elif puntos >= 0.5 and puntos < 1.15:
	grado = "D"
elif puntos >= 1.5 and puntos < 1.5:
	grado = "D+"
elif puntos >= 1.5 and puntos < 1.85:
	grado = "C-"
elif puntos >= 1.85 and puntos < 2.15:
	grado = "C"
elif puntos >= 2.15 and puntos < 2.5:
	grado = "C+"
elif puntos >= 2.5 and puntos < 2.85:
	grado = "B-"
elif puntos >= 2.85 and puntos < 3.15:
	grado = "B"
elif puntos >= 3.15 and puntos < 3.5:
	grado = "B+"
elif puntos >= 3.5 and puntos < 3.85:
	grado = "A-"
elif puntos >= 3.85 and puntos < 4.0:
	grado = "A"
elif puntos >= 4.0:
	grado = "A+"
	
if grado != "":
	print("Tu calificacion es: ",(grado))
else:
	print("Números de punto de califiacion no validos.")