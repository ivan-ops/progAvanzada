#Ejercicio 61. promedio.

a = 1
sumatoria = 0
i = 0

while a != 0:
    a = int(input('inserte un valor'))
    sumatoria = sumatoria + a
    i = i + 1

    promedio = sumatoria / i
    print('el promedio es : ', promedio)
    