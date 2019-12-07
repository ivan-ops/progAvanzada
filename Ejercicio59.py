#Ejercicio 59
#En una jurisdicci�n particular, las matr�culas m�s antiguas consisten en tres letras may�sculas seguidas de tres n�meros. 
#Cuando todas las placas que siguieron ese patr�n ten�an Una vez utilizado, 
#el formato se cambi� a cuatro n�meros seguidos de tres letras may�sculas.

#Escriba un programa que comience leyendo una cadena de caracteres del usuario. 
#Luego, su programa debe mostrar un mensaje que indique si los caracteres son v�lidos 
#para una placa de estilo anterior o una placa de estilo m�s nueva. 
#Su programa debe mostrar un mensaje apropiado si la cadena ingresada por el usuario no es v�lida para ninguno de los estilos de matr�cula.

matricula = input("Introduce la matricula: ")

estilo = ""

if matricula[0] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[1] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[2] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
	if matricula[3] in "0123456789" and matricula[4] in "0123456789" and matricula[5] in "0123456789":
		estilo = "viejo"

elif matricula[0] in "0123456789" and matricula[1] in "0123456789" and matricula[2] in "0123456789" and matricula[3] in "0123456789":
	if matricula[4] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[5] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and matricula[6] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
		estilo = "nuevo"
		
if estilo == "viejo":
	print("Esta es una placa de estilo antiguo.")
elif estilo == "nuevo":
	print("Esta es una placa de estilo nuevo.")
else:
	print("Matr�cula no v�lida ingresada.")