#Ejercicio 51
#En una universidad en particular, las calificaciones con letras se asignan a los puntos de calificaci�n de la siguiente manera:
#Escriba un programa que comience leyendo una calificaci�n de letra del usuario. 
#Luego, su programa debe calcular y mostrar el n�mero equivalente de puntos de calificaci�n. 
#Aseg�rese de que su programa genere un mensaje de error apropiado si el usuario ingresa una calificaci�n de letra no v�lida.

grado = input("Inserta la letra: ")

punto = -1

if grado == "A+":
	punto = 4.0
if grado == "A":
	punto = 4.0
if grado == "A-":
	punto = 3.7
if grado == "B+":
	punto = 3.3
if grado == "B":
	punto = 3.0
if grado == "B-":
	punto = 2.7
if grado == "C+":
	punto = 2.3
if grado == "C":
	punto = 2.0
if grado == "C-":
	punto = 1.7
if grado == "D+":
	punto = 1.3
if grado == "D":
	punto = 1.0
if grado == "F":
	punto = 0
	
if punto >= 0:
	print("Tu calificaion es ",(punto))
else:
	print("Calificaicon ingresada es invalida.")
� 2019 GitHub, Inc.