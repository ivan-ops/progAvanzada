# Ejercicio 14
# Muchas personas piensan en su altura en pies y pulgadas, incluso en algunos países que utilizan principalmente el sistema métrico. 
# Escriba un programa que lea un número de pies del usuario, seguido de un número de pulgadas. 
# Una vez que se leen estos valores, su programa, debe calcular y mostrar el número equivalente de centímetros.
# Sugerencia: un pie mide 12 pulgadas. Una pulgada es 2.54 centímetros.



pies = int(input('Introduce el numero en pies: '))
pulgadas = int(input('Introduce el numero en pulgadas: '))


pulgadas += pies * 12


centimetros = pulgadas * 2.54



print('La altura es: ',(centimetros), 'cm')