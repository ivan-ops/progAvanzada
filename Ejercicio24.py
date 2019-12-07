# Ejercicio 24

# Crear un programa que le pida al usurario la duracion en dias. horas. minutos y segundos.
# Calcular y desplegar la cantidad total de segundos de duracion 


dias = int(input('Introduce los dias: '))
horas = int(input('Introduce los horas: '))
minutos = int(input('Introduce los minutos: '))
segundos = int(input('Introduce los segundos: '))


d = dias*86400

h = horas*3600

m = minutos * 60

s = segundos*1

total = d+h+m+s 

print('\n El total en segundos es: %.2f.' %total ) 