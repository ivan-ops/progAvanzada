# Ejercicio 97
#Usando sus soluciones para los Ejercicios 94 y 96, escriba un programa que genere una buena contraseña aleatoria y la muestre. 
#Cuente y muestre el número de intentos necesarios antes de que se generara una buena contraseña. 
#Estructura tu solución para que importe las funciones que escribiste anteriormente y 
#luego las llame desde una función llamada main en el archivo que crees para este ejercicio.

from ejercicio94 import randomPassword
from ejercicio96 import checkPassword

def main(): 
    n = 0
    passw = ''
    while not checkPassword(passw): 
        passw = randomPassword()
        n = n+1
    print("Intentos: ", n)
    print("Password: ", passw)
    
main()