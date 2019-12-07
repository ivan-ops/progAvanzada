# Ejercicio 21

# El área de un triángulo se puede calcular usando la siguiente fórmula, donde b es la longitud de la base del triángulo y h es su altura:
# área = b × h / 2
# Escriba un programa que permita al usuario ingresar valores para b y h. Luego, el programa debe calcular y mostrar el área de un triángulo con longitud base b y altura h.



b = float(input('Inserte la longitud de la base del triangulo: '))
h = float(input('Inserte la altura del triangulo: '))


a = (b*h)/2


print('\n El area del triangulo es: %.2f'%a,'unidades cuadradas')