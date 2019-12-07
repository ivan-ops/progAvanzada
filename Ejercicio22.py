# Ejercicio 22

# En el ejercicio anterior, se creó un programa que calculaba el área de un triángulo cuando se conocía la longitud de su base y su altura. 
# También es posible calcular el área de un triángulo cuando se conocen las longitudes de los tres lados. 
# Sean s1, s2 y s3 
# las longitudes de los lados. 
# Sea s = (s1 + s2 + s3) / 2. 
# Entonces el área del triángulo se puede calcular usando la siguiente fórmula:
# área = sqrt (s × (s - s1) × (s - s2) × (s - s3))
# Desarrolle un programa que lea las longitudes de los lados de un triángulo del usuario y muestre su área.



from math import sqrt


s1 = float(input('Inserte la longitud del lado 1 del triangulo: '))
s2 = float(input('Inserte la longitud del lado 2 de triangulo: '))
s3 = float(input('Inserte la longitud del lado 3 de triangulo: '))


s = (s1 + s2 + s3)/2
a = sqrt (s*(s-s1)*(s-s2)*(s-s3))


print('El area del triangulo es: %.2f'%a,'unidades cuadradas')
