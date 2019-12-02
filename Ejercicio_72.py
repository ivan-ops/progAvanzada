# Ejercicio 72
#Una cadena es un palíndromo si es idéntica hacia adelante y hacia atrás. 
#Por ejemplo, "anna", "civic", "level" y "hannah" son ejemplos de palabras palindrómicas. 
#Escriba un programa que lea una cadena del usuario y use un bucle para determinar si es o no un palíndromo. 
#Muestra el resultado, incluido un mensaje de salida significativo.
palabra = input('Introduce la palabra: ')
palindromo = palabra [::-1]
if palindromo == palabra:
    print('la palabra',palabra, 'es un palindromo')
else:
    print('la plabra',palabra, 'no es un palindromo')