# Ejercicio 12
# Distancia entre dos puntos de la tierra
# La superficie de la tierra es curva y la distancia entre grados de longitud varia con la latitud.
# Como resultado, encontrar la distancia entre dos puntos de la superficide de la tierra es mas complicado que usar el teorema de pitagoras.
# Si (t1,g1) y (t2,g2) es la latitud y longitud de dos puntos de la superficie de la tierra.
# La distancia entre esos puntos, a traves de la superficie de la tierra, en kilometros es:
# distancia = 6271.01*arccos(sen(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2))
# cree un programa que le permita al usuario introducir la latitud y la longitud de dos puntos de la tierra en grados.
# su programa debe desplegar la distancia entre esos dos puntos, en kilometros.
# Tenga cuenta que las funciones trigonometricas en python trabajan en radianes, por lo tanto se debe convertir su valor introducido
# por el usuario en grados a radianes antes de utilizar la formula.
# El modulo math contiene el comando radianes, que cambia de grados a radianes.
# * todo from math
from math import radians, cos, sin, asin, sqrt





print("Introduce la latitud y longitud :")
lat1 = float(input(" Latitud 1:        "))
lon1 = float(input(" Longitud 1:       "))
lat2 = float(input(" Latitud 2:        "))




lon2 = float(input(" Longitud 2:       "))






lon1 = radians(lon1)
lon2 = radians(lon2)
lat1 = radians(lat1)
lat2 = radians(lat2)



dlon = lon2 - lon1 
dlat = lat2 - lat1 
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * asin(sqrt(a)) 
r = 6371 
 




print('Distancia es:      %.2f.' %(c*r),'Kilometros')







