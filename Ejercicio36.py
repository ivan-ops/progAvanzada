# Ejercicio 36

# En este ejercicio creará un programa que lee una letra del alfabeto del usuario. 
# Si el usuario ingresa a, e, i, o, u, entonces su programa debe mostrar un mensaje que indica que la letra ingresada es una vocal. 
# Si el usuario ingresa Y entonces su programa debería mostrar un mensaje que indica que a veces Y es una vocal, y a veces Y es una consonante. 
# De lo contrario, su programa debería mostrar un mensaje indicando que la letra es una consonante.




letra = input('Introduce una letra del abecedario: ')



if letra in 'aeiou':
	print('Esta letra es una vocal')
elif letra == 'y':
    print('A veces es una vocal y a veces una consonante')
else:
	print('Esta letra es una consonante')