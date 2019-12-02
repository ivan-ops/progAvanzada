# Ejercicio 64
#El 4 de febrero de 2013 fue el último día en que Royal Canadian Mint distribuyó centavos. 
#Ahora que los centavos se han eliminado, 
#los minoristas deben ajustar los totales para que sean múltiplos de 5 centavos cuando se pagan en efectivo 
#(las transacciones con tarjeta de crédito y débito se siguen cargando al centavo). 
#Si bien los minoristas tienen cierta libertad en cómo lo hacen, la mayoría elige redondear al níquel más cercano.
#Escriba un programa que lea los precios del usuario hasta que se ingrese una línea en blanco. 
#Muestre el costo total de todos los artículos ingresados en una línea, 
#seguido del monto adeudado si el cliente paga con efectivo en una segunda línea. 
#El monto adeudado por un pago en efectivo debe redondearse al níquel más cercano. 
#Una forma de calcular el monto del pago en efectivo es comenzar determinando cuántos centavos se necesitarían para pagar el total. 
#Luego calcule el resto cuando este número de centavos se divide por 5. 
#Finalmente, ajuste el total hacia abajo si el resto es menor que 2.5. De lo contrario, ajuste el total hacia arriba.
suma = 0
sumaredondeada = 0

interrumpido = False 
while not interrumpido:
	precio = input("Introduce el precio: ")
	
	if precio != "":
		precio = float(precio)
	else:
		break
		
	suma += precio 
	
	penique = precio * 100
	recorda = penique % 5
	
	if recorda > 2.5:
		penique += 5 - recorda 
	else:
		penique -= recorda 
	
	redondeado = penique * 0.01
	sumaredondeada += redondeado

print("El costo actual es: %.2f" %(suma))
print("Pagando en efectivo: %.1f" %(sumaredondeada))
