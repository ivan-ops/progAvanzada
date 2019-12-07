
# Ejercicio 20 

# La ley de los gases ideales es una aproximación matemática del comportamiento de los gases 
# a medida que cambian la presión, el volumen y la temperatura. 
# Por lo general, se indica como:
# PV = nRT
# Donde P es la presión en Pascales, V es el volumen en litros, n es la cantidad de sustancia en moles, 
# R es la constante de gas ideal, igual a 8.314 J mol K, y T es la temperatura en grados Kelvin.
# Escriba un programa que calcule la cantidad de gas en moles cuando el usuario suministra la presión, el volumen y la temperatura. 
# Pruebe su programa determinando la cantidad de moles de gas en un tanque de buceo. 
# Un tanque típico de SCUBA contiene 12 litros de gas a una presión de 20,000,000 Pascales (aproximadamente 3,000 PSI). 
# La temperatura ambiente es de aproximadamente 20 grados Celsius o 68 grados Fahrenheit.


P = float(input('Inserte la presion en pascales: '))

V = float(input('Inserte el volumen en litros: '))

T = float(input('Inserte la temperatura en celsius: '))

R = 8.314

t = T + 273.15

n = (P*V) / (R*t)


print('La cantidad de gas en esas condiciones es: %.2f' %(n), 'moles')