## Ejercicio 28

# Cuando el viento sopla en clima frío, el aire se siente aún más frío de lo que realmente es
# porque el movimiento del aire aumenta la velocidad de enfriamiento de los objetos cálidos, como las personas. 
# Este efecto se conoce como sensación térmica.
# En 2001, Canadá, el Reino Unido y los Estados Unidos adoptaron la siguiente fórmula para calcular el índice de sensación térmica. 
# Dentro de la fórmula “Ta” está la temperatura del aire en grados Celsius y “V” es la velocidad del viento en kilómetros por hora.
# WCI = 13.12 + 0.6215Ta − 11.37V^0.16 + 0.3965TaV^0.16



aire = float(input('Introudce la temperatura del aire: '))
viento = float(input('Introduce la velocidad del viento: '))


ist = 13.12 + (0.6215*aire) - (11.37*(viento**0.16)) + (0.3965*aire*(viento**0.16))


print('El IST (Indice de sencaion termica) es ', round(ist))
