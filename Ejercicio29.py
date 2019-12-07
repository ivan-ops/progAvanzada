# Ejercicio 29

# Escriba un programa que comience leyendo una temperatura del usuario en grados Celsius. 
# Luego, su programa debe mostrar la temperatura equivalente en grados Fahrenheit y grados Kelvin. 
# Los cálculos necesarios para convertir entre diferentes unidades de temperatura se pueden encontrar en Internet.


celsius = float(input('Introduce la temperatura en celsius: '))



fahrenheit = celsius * (9/5) + 32
kelvin = celsius + 273.15



print('\n En Fahrenheit: %.2f' %(fahrenheit))
print('\n En Kelvin:    ',(kelvin))