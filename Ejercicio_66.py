# Ejercicio 66
#El ejercicio 51 incluyó una tabla que muestra la conversión de calificaciones 
#de letras a puntos de calificación en una institución académica particular. 
#En este ejercicio calculará el promedio de calificaciones de un número arbitrario de calificaciones de letras ingresadas por el usuario. 
#El usuario ingresará una línea en blanco para indicar que se han proporcionado todas las calificaciones. 
#Por ejemplo, si el usuario ingresa A, seguido de C +, seguido de B, seguido de una línea en blanco, 
#su programa debe informar un promedio de calificaciones de 3.1.
#Puede encontrar útil su solución para el ejercicio 51 al completar este ejercicio. S
#u programa no necesita hacer ninguna comprobación de errores. 
#Se puede suponer que cada valor ingresado por el usuario siempre será una calificación de letra válida o una línea en blanco.

calificaciones = []

while True:
    calificacion = input("Introduce la calificacion: ")

    puntos = 0

    if calificacion == "":
        break
    if calificacion == "A+":
        puntos = 4.0
    if calificacion == "A":
        puntos = 4.0
    if calificacion == "A-":
        puntos = 3.7
    if calificacion == "B+":
        puntos = 3.3
    if calificacion == "B":
        puntos = 3.0
    if calificacion == "B-":
        puntos = 2.7
    if calificacion == "C+":
        puntos = 2.3
    if calificacion == "C":
        puntos = 2.0
    if calificacion == "C-":
        puntos = 1.7
    if calificacion == "D+":
        puntos = 1.3
    if calificacion == "D":
        puntos = 1.0
    if calificacion == "F":
        puntos = 0
    
    calificaciones.append(puntos)

total = 0 
num = 0
for calificacion in calificaciones:
    total += calificacion 
    num += 1

promedio = total / num 

print("Tu promedio de calificaciones es: ",(promedio))