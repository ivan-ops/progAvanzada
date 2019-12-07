# Ejercicio 18
# El volumen de un cilindro se puede calcular multiplicando el área de su base circular por su altura. 
# Escriba un programa que lea el radio del cilindro, junto con su altura, del usuario y calcule su volumen. 
# Muestra el resultado redondeado a un decimal.


from math import pi


radio = float(input('Introduce el radio del clindro: '))


altura = float(input('Introduce la altura del cilindro: '))


volumen = pi * (radio**2) * altura


print('El volumen del cilindro es: %0.01f '%(volumen))