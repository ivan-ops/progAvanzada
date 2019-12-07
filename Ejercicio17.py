# Ejercicio 17
# La cantidad de energía requerida para aumentar la temperatura de un gramo de un material en un grado Celsius es la capacidad de calor específica del material, C. 
# La cantidad total de energía requerida para elevar m gramos de un material en ΔT grados Celsius 
# Se puede calcular usando el fórmula:
# q = mCΔT.
# Escriba un programa que lea la masa de un poco de agua y el cambio de temperatura del usuario. 
# Su programa debe mostrar la cantidad total de energía que debe agregarse o eliminarse para lograr el cambio de temperatura deseado.
# Sugerencia: La capacidad calorífica específica del agua es 4.186 J g◦C. 
# Debido a que el agua tiene una densidad de 1.0 gramo por mililitro, puede usar gramos y mililitros de manera intercambiable en este ejercicio.

# Extienda su programa para que también calcule el costo de calentar el agua. 
# La electricidad se factura normalmente utilizando unidades de kilovatios hora en lugar de julios.
# En este ejercicio, debe asumir que la electricidad cuesta 8.9 centavos por kilovatio-hora. 
# Use su programa para calcular el costo de hervir agua para una taza de café.
# Sugerencia: Deberá buscar el factor para convertir entre julios y kilovatios hora para completar la última parte de este ejercicio.

masa = float(input('Introduce la masa del agua en gramos: '))
cambio_temp = float(input('Introduce el cambio de temperatura en grados celcius: '))

C = 4.186 
julios = masa * C * cambio_temp


print("\n El total de energia en julios es: ",(julios))


costo_kilowat_hora = 8.9 

kilowat_hora = julios / 3.6e+6 

costo = kilowat_hora * costo_kilowat_hora

print("\n El costo total es: $",(costo))