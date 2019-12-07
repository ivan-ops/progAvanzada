#Ejercicio 60
#Una ruleta tiene 38 espacios. De estos espacios, 18 son negros, 18 son rojos y dos son verdes. Los espacios verdes están numerados 0 y 00. 
#Los espacios rojos están numerados 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 y 36. 
#los números enteros restantes entre 1 y 36 se usan para numerar los espacios negros.
#Se pueden hacer muchas apuestas diferentes en la ruleta. Solo consideraremos el siguiente subconjunto de ellos en este ejercicio:
#• Número único (1 a 36, 0 o 00)
#• Rojo contra negro
#• Impar versus par (tenga en cuenta que 0 y 00 no pagan por par)
#• 1 a 18 versus 19 a 36
#Escriba un programa que simule el giro de una rueda de ruleta utilizando el generador de números aleatorios de Python. "random.randint"
#Muestra el número que se seleccionó y todas las apuestas que se deben pagar. Por ejemplo, si se selecciona 13, su programa debería mostrar:
#El giro resultó en 13 ...
#Pagar 13
#Pagar negro
#Paga impar
#Pague de 1 a 18
#Si la simulación da como resultado 0 o 00, su programa debería mostrar Pay 0 o Pay 00 sin ningún resultado adicional.

import random

giro = random.randint(0, 37)

if giro == 0:
	if random.randint(0, 2) == 0:
		print("paga 00")
	else:
		print("paga 0")
		
else:
	print("El giro resultó en {}...".format(giro))

	print("paga {}".format(giro))
	
	if giro == 1 or giro == 3 or giro == 5 or giro == 7 or giro == 9 or giro == 12 or giro == 14 or giro == 16 or giro == 18 \
	or giro == 19 or giro == 21 or giro == 23 or giro == 25 or giro == 27 or giro == 30 or giro == 32 or giro == 34 or giro == 36:
		print("paga rojo")
	else:
		print("paga negro")
		
	if giro > 0:
		if giro % 2 == 0:
			print("paga par")
		else:
			print("Paga impar")
	
	if giro >= 1 and giro <= 18:
		print("paga 1 a 18")
	elif giro >= 19 and giro < 36:
		print("paga 19 a 36")