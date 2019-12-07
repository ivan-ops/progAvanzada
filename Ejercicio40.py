# Ejercicio 40

# Un triángulo se puede clasificar en función de la longitud de sus lados como equilátero, isósceles o escaleno. 
# Los 3 lados de un triángulo equilátero tienen la misma longitud. 
# Un triángulo isósceles tiene dos lados que tienen la misma longitud y un tercer lado que tiene una longitud diferente. 
# Si todos los lados tienen diferentes longitudes, entonces el triángulo es escaleno. 
# Escriba un programa que lea las longitudes de 3 lados de un triángulo del usuario. 
# Muestra un mensaje que indica el tipo de triángulo.



l1 = float(input('Introduce la longitud del primer lado del triangulo: '))
l2 = float(input('Introduce la longitud del segundo lado del triangulo: '))
l3 = float(input('Introduce la longitud del tercer lado del triangulo: '))




if l1 == l2 == l3:
	triangulo = "Equilatero"
elif l1 == l2 or l1 == l3 or l2 == l3:
	triangulo = "Isoseles"
else:
	triangulo = "Escaleno"
	
print('Es un triangulo: ',(triangulo))