# Ejercicio 47
# Los horóscopos comúnmente reportados en los periódicos usan la posición del sol en el momento del nacimiento 
# para intentar predecir el futuro. 
# Este sistema de astrología divide el año en doce signos del zodiaco, 
# como se describe en la tabla a continuación:
# |Zodiac sign | Date range |
# |Capricorn |December 22 to January 19| 
#|Aquarius |January 20 to February 18| 
#|Pisces |February 19 to March 20| 
#|Aries |March 21 to April 19| 
#|Taurus |April 20 to May 20| 
#|Gemini |May 21 to June 20| 
#|Cancer |June 21 to July 22| 
#|Leo |July 23 to August 22| 
#|Virgo |August 23 to September 22| 
#|Libra |September 23 to October 22| 
#|Scorpio |October 23 to November 21| 
#|Sagittarius |November 22 to December 21|
# Escriba un programa que le pida al usuario que ingrese su mes y día de nacimiento. 
# Luego, nuestro programa debe informar el signo zodiacal del usuario como parte de un mensaje de salida apropiado.

mes = int(input('Introduce el mes de tu nacimiento: '))
dia = int(input('Introduce el dia de tu nacimiento: '))

mes <= 12 and mes >= 1
dia <= 31 and mes >= 1


zodiaco = ""

if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
	zodiaco = "Capricornio"
	
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
	zodiaco = "Aquario"
	
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
	zodiaco = "Piscis"
	
elif (mes == 3 and dia >= 21) or (mes == 4 and dai <= 19):
	zodiaco = "Aries"
	
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
	zodiaco = "Tauro"

elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
	zodiaco = "Geminis"
	
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
	zodiaco = "Cancer"
	
elif (mes == 7 and dia <= 23) or (mes == 8 and dia <= 22):
	zodiaco = "Leo"
	
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
	zodiaco = "Virgo"
	
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
	zodiaco = "Libra"
	
elif (mes == 10 and dia <= 23) or (mes == 11 and dia <= 21):
	zodiaco = "Escorpion"
	
elif (mes == 11 and dia <= 22) or (mes == 12 and dia <= 21):
	zodiaco = "Sagitario"
    
	
print('Tu signo zodiacal es:  ',(zodiaco))