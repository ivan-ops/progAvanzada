# Ejercicio 23

# Un polígono es regular si sus lados tienen la misma longitud y los ángulos entre todos los lados adyacentes son iguales. 
# El área de un polígono regular se puede calcular usando la siguiente fórmula, donde s es la longitud de un lado y n es el número de lados:
# área = (n × s^2) / (4 × tan (π/ n))
# Escriba un programa que lea s y n del usuario y luego muestre el área de un polígono regular construido a partir de estos valores.



from math import tan, pi
s = float(input('Inserte la longitud de un lado: '))
n = float(input('Inserte el numero de lados: '))


a = (n*s**2)/(4*tan(pi/n))


print('\n El area del poligono regular es: %.2f' %a ,'unidades cuadradas')