# Ejercicio 39

# Escriba un programa que lea un nivel de sonido en decibelios del usuario. 
# Si el usuario ingresa un nivel de decibelios que coincide con uno de los ruidos en la tabla, 
# entonces su programa debería mostrar un mensaje que contenga solo ese ruido. 
# Si el usuario ingresa una cantidad de decibelios entre los ruidos enumerados, 
# entonces su programa debe mostrar un mensaje que indique entre qué ruidos se encuentra el nivel. 
# Asegúrese de que su programa también genere una salida razonable para un valor menor que el ruido más bajo de la tabla 
# y para un valor mayor que el ruido más alto de la tabla.




dbLevel = float(input('Introduce el nivel de dB: '))



if dbLevel < 40:
	print('Muy bajo')

elif dbLevel == 40:
	print('Cuarto tranquilo')    

elif dbLevel > 40 and dbLevel <= 69 :
	print('Esta entre cuarto tranquilo y despertador')

elif dbLevel == 70:
	print('Despertador')

elif dbLevel > 70 and dbLevel <= 105:
	print('Esta entre despertador y costa cesped') 

elif dbLevel == 106:
	print('Corta cesped')

elif dbLevel > 106 and dbLevel <= 129:
	print('Esta entre corta cesped y martillo neumatico')

elif dbLevel == 130:
	print('Martillo neumatico')   

elif dbLevel > 130:
	print('Muy ruidos')
	
	




	






