#Ejercicio 55
#La radiación electromagnética se puede clasificar en una de las 7 categorías según su frecuencia, 
#como se muestra en la tabla a continuación:

#Escriba un programa que lea la frecuencia de la radiación del usuario y muestre el nombre apropiado.

frecuencia = float(input("Introduce la frecuencia: "))

categoria = ""

if frecuencia < 3e9:
	categoria = "Ondas de radio"
elif frecuencia >= 3e9 and frecuencia < 3e12:
	categoria = "microondas"
elif frecuencia >= 3e12 and frecuencia < 4.3e14:
	categoria = "Luz infraroja"
elif frecuencia >= 4.3e14 and frecuencia < 7.5e14:
	categoria = "Luz visible"
elif frecuencia >= 7.5e14 and frecuencia < 3e17:
	categoria = "Luz ultravioleta"
elif frecuencia >= 3e17 and frecuencia < 3e19:
	categoria = "Rayos-X"
elif frecuencia >= 3e19:
	categoria = "Rayos gamma"
	
if categoria != "":
	print("Esta frecuencia esta en la categoria de: ",(categoria))
else:
	print("Frecuencia introducida invalida.")