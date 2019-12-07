# Ejercicio 31

# Desarrolle un programa que lea un número entero de cuatro dígitos del usuario y muestre la suma de los dígitos en el número. 
# Por ejemplo, si el usuario ingresa 3141, entonces su programa debería mostrar 3 + 1 + 4 + 1 = 9.



numero = input('Introduce un numero entero de 4 digitos: ')


a  = int(numero[0])
a  += int(numero[1])
a += int(numero[2])
a += int(numero[3])


print(numero[0], '+', numero[1], '+', numero[2], '+', numero[3], '=',a)
