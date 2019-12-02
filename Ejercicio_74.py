# Ejercicio 74
#En este ejercicio, creará un programa que muestra una tabla de multiplicación 
#que muestra los productos de todas las combinaciones de enteros desde 1 por 1 hasta 10 inclusive 10. 
#Su tabla de multiplicación debe incluir una fila de etiquetas en la parte superior que contenga números del 1 al 10. 
#También debe incluir etiquetas en el lado izquierdo que consisten en los números del 1 al 10. 
#La salida esperada del programa se muestra a continuación:
#| |1|2|3|4|5|6|7|8|9|10|
#|1|1|2|3|4|5|6|7|8|9|10|
#|2|2|4|6|8|10|12|14|16|18|20|
#|3|3|6|9|12|15|18|21|24|27|30|
#|4|4|8|12|16|20|24|28|32|36|40|
#|5|5|10|15|20|25|30|35|40|45|50|
#|6|6|12|18|24|30|36|42|48|54|60|
#|7|7|14|21|28|35|42|49|56|63|70|
#|8|8|16|24|32|40|48|56|64|72|80|
#|9|9|18|27|36|45|54|63|72|81|90|
#|10|10|20|30|40|50|60|70|80|90|100|
#Al completar este ejercicio, probablemente le sea útil poder imprimir un valor sin pasar a la siguiente línea. 
#Esto se puede lograr agregando end = " " como el último parámetro a su declaración de impresión. 
#Por ejemplo, print ("A") mostrará la letra A y luego bajará a la siguiente línea. 
#La instrucción de impresión ("A", end = "") mostrará la letra A sin moverse a la línea siguiente, 
#haciendo que la siguiente instrucción de impresión muestre su resultado en la misma línea que la letra A

min = 1
max = 10
print('     ',end='')
for i in range(min, max +1):
    print('%4d' % i, end=' ')
print()

for i in range(min, max +1):
    print('%4d' % i, end=' ')
    for j in range(min, max +1):
        print('%4d' %(i*j), end=' ')
    print()