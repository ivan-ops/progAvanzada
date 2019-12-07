#Ejercicio 53
#En una empresa en particular, los empleados son calificados al final de cada a�o. 
#La escala de calificaci�n comienza en 0.0, con valores m�s altos que indican un mejor rendimiento y que resultan en aumentos mayores.
#El valor otorgado a un empleado es 0.0, 0.4 o 0.6 o m�s. Los valores entre 0.0 y 0.4, y entre 0.4 y 0.6 nunca se usan. 
#El significado asociado con cada calificaci�n se muestra en la siguiente tabla. 
#El monto del aumento de un empleado es de $ 2400.00 multiplicado por su calificaci�n.
#Escriba un programa que lea una calificaci�n del usuario e indique si el rendimiento fue inaceptable, aceptable o meritorio. 
#Tambi�n se debe informar el monto del aumento del empleado. 
#Su programa debe mostrar un mensaje de error apropiado si se ingresa una calificaci�n no v�lida.

valor = float(input("Introduce la calificacion del empleado: "))

Rendimiento = ""

if valor == 0.0:
	Rendimiento = "Rendimiento inaceptable"
elif valor == 0.4:
	Rendimiento = "Rendimiento aceptable"
elif valor >= 0.6:
	Rendimiento = "Rendimiento meritorio"

if Rendimiento != "":
	print("De acuerdo a al escala el empleado ha demostrado tener: ",(Rendimiento))
else:
	print("Valor introducido no v�lido (El valor es 0.0, 0.4 o mayor que 0.6)")
if valor==0.0 or valor== 0.4 or valor >=0.6:
    monto = 2400 * valor
    print('El monto total del aumento es: ', monto)