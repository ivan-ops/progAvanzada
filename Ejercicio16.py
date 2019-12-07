# Ejercicio 16
# Escriba un programa que comience leyendo un radio, r, del usuario. 
# El programa continuará calculando y mostrando el área de un círculo con radio r y el volumen de una esfera con radio r. 
# Use la constante pi en el módulo matemático en sus cálculos.
# Sugerencia: El área de un círculo se calcula usando el área de fórmula = π*r^2. 
# El volumen de una esfera se calcula usando la fórmula volumen = 4/3 * π* r^3.




from math import pi




r = float(input('Introduce el radio: '))



area = pi * r**2
vol = (4/3) * (pi * r**3)




print("El area de un circulo es:     %.3f." %(area),'unidades cuadradas')
print("El volumen de un circulo es: %.3f." %(vol),'unidades al cubo')