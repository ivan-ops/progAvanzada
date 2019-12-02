# Ejercicio 63
#Escriba un programa que muestre una tabla de conversión de temperatura para grados Celsius y grados Fahrenheit. 
#La tabla debe incluir filas para todas las temperaturas entre 0 y 100 grados centígrados que son múltiplos de 10 grados centígrados. 
#Incluya encabezados apropiados en sus columnas. 
#La fórmula para convertir entre grados Celsius y grados Fahrenheit se puede encontrar en Internet.
#la fornula es fahrenheit = (celsius * 9/5) + 32

print("Celsius\t | Fahrenheit")

for celsius in range(0, 101, 10):
	fahrenheit = (celsius * 9/5) + 32
	
	print(celsius,'\t','|' ,fahrenheit)
