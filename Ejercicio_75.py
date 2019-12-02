# Ejercicio 75
#El máximo común divisor de dos enteros positivos, n y m, es el número más grande, d, que se divide uniformemente en n y m. 
#Existen varios algoritmos que pueden usarse para resolver este problema, que incluyen:
# Inicialice d al menor de m y n.
# while d no divide equitativamente m o d no divide equitativamente n do
# Disminuya el valor de d en 1
# Informe d como el máximo divisor común de n y m
#Escriba un programa que lea dos enteros positivos del usuario y use este algoritmo para determinar e informar su máximo divisor común.

n = int(input('Introduce un numero entero pocitivo: '))

m = int(input('Introduce un numero entero pocitivo: '))

d = min(n,m)

while n % d !=0 or m % d != 0:
    d = d-1
print('El maximo divisor comun de ', n, 'y ', m,'es:',d )