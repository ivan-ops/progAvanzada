# Ejercicio 61
# En este ejercicio usted creara un programa que calcule el promedio de una colección de valores insertados por el usuario, 
# si el usuario introduce el valor cero el programa debe dejar de pedir valores y posteriormente, mostrar el promedio calculado.
a = 1
sumatoria = 0
i = 0
while a !=0:
    a = int(input('Inserte un valor: '))
    sumatoria = sumatoria + a
    i = i + 1
promedio = sumatoria / (i-1)
print('El promedio es', promedio)
