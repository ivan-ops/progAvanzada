# Ejercicio 25

# En este ejercicio usted revertira el proceso descrito en el ejercicio previo.
# Desarrolle un programa que comnienze por leer una cantidad en segundos introducidos por el usuario. 
# Su programa debe desplegar la cantidad equivlente en forma de D:HH:NN:SS, 
# Donde D son los dias, HH las horas, MM los minutos y SS los segundos.
# Las horas, minutos y segundos deben estar en formato de 2 digitos, con un 0 al inicio, si es necesario.



d = 86400 

h = 3600 

m = 60 

segundos = int(input('Introduce los segundos: '))




dias = segundos / d
segundos = segundos % d

horas = segundos / h
segundos = segundos % h

minutos = segundos / m
segundos = segundos % m



print('\n %d:%02d:%02d:%02d.' %(dias, horas, minutos, segundos))