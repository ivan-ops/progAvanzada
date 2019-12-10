# Ejercicio 100
#Escriba una función que determine cuántos días hay en un mes en particular. 
#Su función tomará dos parámetros: el mes como un número entero entre 1 y 12, y el año como un número entero de cuatro dígitos. 
#Asegúrese de que su función informa el número correcto de días en febrero para los años bisiestos. 
#Incluya un programa principal que lea un mes y un año del usuario y muestre la cantidad de días en ese mes. 
#Puede encontrar útil su solución para el ejercicio 57 al resolver este problema
from ejercicio57 import ano_bisi as ano

def days_in_month(month, year): 
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    feb = 2
    
    if month in days_31: 
        print("Este mes tiene 31 días")
    elif month in days_30: 
        print("Este mes tiene 30 días")
    elif month == feb: 
        if ano(year): 
            print("Este mes tiene 29 días")
        else: 
            print("Este mes tiene 28 días")
          
    
