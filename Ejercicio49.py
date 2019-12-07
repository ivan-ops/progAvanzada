# Ejercicio 49
# La siguiente tabla contiene rangos de magnitud de terremotos en la escala de Richter y sus Tipos:
# Magnitude Tipos 
# Less than 2.0 Micro 
#2.0 to less than 3.0 Very minor 
#3.0 to less than 4.0 Minor 
#4.0 to less than 5.0 Light 
#5.0 to less than 6.0 Moderate 
#6.0 to less than 7.0 Strong 
#7.0 to less than 8.0 Major
#8.0 to less than 10.0 Great 
#10.0 or more Meteoric
# Escriba un programa que lea una magnitud del usuario y muestre el descriptor apropiado como parte de un mensaje significativo. 
# Por ejemplo, si el usuario ingresa 5.5, 
# entonces su programa debe indicar que un terremoto de magnitud 5.5 se considera un terremoto moderado



magnitud = float(input('Introduce la magniutd del terremoto: '))

if magnitud < 2.0:
	tipo = "Micro"
elif magnitud >= 2.0 and magnitud < 3.0:
	tipo = "Muy suabe"
elif magnitud >= 3.0 and magnitud < 4.0:
	tipo = "Suabe"
elif magnitud >= 4.0 and magnitud < 5.0:
	tipo = "Ligero"
elif magnitud >= 5.0 and magnitud < 6.0:
	tipo = "Moderado"
elif magnitud >= 6.0 and magnitud < 7.0:
	tipo = "Fuerte"
elif magnitud >= 7.0 and magnitud < 8.0:
	tipo = "Mayor"
elif magnitud >= 8.0 and magnitud < 10.0:
	tipo = "Grande"
else:
	tipo = "Meteorico"
	
print('Un terremoto de ',(magnitud), 'se considera', (tipo))
