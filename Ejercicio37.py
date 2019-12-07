# Ejercicio 37 

# Escriba un programa que determine el nombre de una forma a partir de su número de lados. 
# Lea el número de lados del usuario y luego informe el nombre apropiado como parte de un mensaje significativo. 
# Su programa debe admitir formas desde 3 hasta 10 lados. 
# Si se ingresa un número de lados fuera de este rango, entonces su programa debería mostrar un mensaje de error apropiado.



lados = int(input('Introduce el numero de lados: '))



if lados == 3:
	print('\n Es un triangulo.')
elif lados == 4:
	print('\n Es un cuadrado.')
elif lados == 5:
	print('\n Es un pentagono.')
elif lados == 6:
	print('\n Es un hexagono.')
elif lados == 7:
	print('\n Es un heptagono.')
elif lados == 8:
	print('\n Es un octagono.')
elif lados == 9:
	print('\n Es un nonagono.')
elif lados == 10:
	print('\n Es un decagono')
else:
	print('\n El numero de lado esta fuera de rango')