## Ejercicio 68
#Un bit de paridad es un mecanismo simple para detectar errores en los datos transmitidos a través de una conexión no confiable, 
#como una línea telefónica. 
#La idea básica es que se transmite un bit adicional después de cada grupo de 8 bits para que se pueda 
#detectar un error de un solo bit en la transmisión.
#Los bits de paridad se pueden calcular para paridad par o paridad impar. 
#Si se selecciona paridad par, se elige el bit de paridad que se transmite de modo que el número total de un bit transmitido 
#(8 bits de datos más el bit de paridad) sea par. Cuando se selecciona paridad impar, 
#se elige el bit de paridad para que el número total de un bit transmitido sea impar.
#Escriba un programa que calcule el bit de paridad para grupos de 8 bits ingresados por el usuario usando paridad par. 
#Su programa debe leer cadenas que contengan 8 bits hasta que el usuario ingrese una línea en blanco. 
#Después de que el usuario ingrese cada cadena, su programa debe mostrar un mensaje claro que indique si el bit de paridad debe ser 0 o 1. 
#Muestre un mensaje de error apropiado si el usuario ingresa algo distinto de 8 bits.

linea = input('Introduce 8 bits: ')

while linea != '':
    if linea.count('0') + linea.count('1') !=8 or len(linea) !=8:
        print('No son 8 bits')
    else:
        uno = linea.count('1')
        if uno % 2== 0:
            print('La paridad de bits deberia de ser 0.')
        else:
            print('La paridad de bits deberia de ser 1')
    linea = input('Introduce 8 bits: ')