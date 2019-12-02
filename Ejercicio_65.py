# Ejercicio 65
#Escribe un programa que calcule el perímetro de un polígono. 
#Comience leyendo los valores x e y para el primer punto en el perímetro del polígono del usuario. 
#Luego, continúe leyendo pares de valores x e y hasta que el usuario ingrese una línea en blanco para la Coordenada x. 
#Cada vez que lea una coordenada adicional, debe calcular la distancia al punto anterior y agregarla al perímetro. 
#Cuando se ingresa una línea en blanco para la coordenada x, 
#su programa debe agregar la distancia desde el último punto de regreso al primer punto al perímetro. 
#Entonces debería mostrar el perímetro total. La entrada y salida de muestra se muestra a continuación, 
#con la entrada del usuario en negrita:
#Ingrese la parte x de la coordenada: 0
#Ingrese la parte y de la coordenada: 0
#Ingrese la parte x de la coordenada: (en blanco para salir): 1
#Ingrese la parte y de la coordenada: 0
#Ingrese la parte x de la coordenada: (en blanco para salir): 0
#Ingrese la parte y de la coordenada: 1
#Ingrese la parte x de la coordenada: (en blanco para salir):
#El perímetro de ese polígono es 3.414213562373095
from math import sqrt
perimetro = 0

x1 = int(input("Introduce la cordenada x: "))
y1 = int(input("Introduce la coordenada y: "))

x2 = x1
y2 = y1

line = input('Introduce la coordenada x, (blanco para quitar): ')
while line !='':
    x = float(line)
    y = float(input('Introuce la coordenada y: '))
    distancia = sqrt((x2-x)**2 + (y2-y)**2)
    perimetro = perimetro + distancia
    x2=x
    y2=y
    line= input('Inroduce la coordenada x, (blanco para quitar): ')
distancia = sqrt((x1-x)**2 + (y1-y)**2)
perimetro = perimetro + distancia
print('El perimetro del poligono es: ', perimetro)