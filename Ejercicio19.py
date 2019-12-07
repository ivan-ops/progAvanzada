# ejercicio 19

# Escriba un programa que determine como un objeto viaja cuando golpea el piso.

# El usuario insertara la informacion de la altura desde donde el objeto se deja caer, en metros(m)

# dado que el objeto se deja caer desde el reposo (Velocidad inicial V0= 0 m/s)

# Asumiendo que l aceleracion debido a la gravedad es 9.81 m/s^2 y usando la formula 

# Vf= raiz (Vo ^2 + 2gd) 

# Calcule la velocidad final Vf usando la velocidad inicial V0 

# la aceleración = g, la distancia = d


from math import sqrt


distancia = float(input('Introduce la altura en metros: '))


g = 9.81


vf = sqrt(2 * g * distancia )


print('\n la velocidad final es: %.2f.' %vf, 'm/s')
