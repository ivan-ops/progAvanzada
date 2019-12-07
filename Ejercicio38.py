## Ejercicio 38


# La duración de un mes varía de 28 a 31 días. 
# En este ejercicio creará un programa que lee el nombre de un mes del usuario como una cadena. 
# Luego, su programa debería mostrar la cantidad de días en ese mes. 
# Muestre “28 o 29 días” para febrero para que se aborden los años bisiestos.



mes = input('Introdice en nombre del mes: ')



if mes == "septiembre" or mes == "abril" or mes == "junio" or mes == "november":
	print('Hay 30 dias en este mes')
elif mes == "febrero":
	print('Hay 28 o 29 dias en este mes')
else:
	print('Hay 31 dias en este mes')