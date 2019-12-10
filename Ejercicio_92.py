# Ejercicio 92
#Un número primo es un número entero mayor que 1 que solo es divisible por uno y por sí mismo. 
#Escriba una función que determine si su parámetro es primo o no, 
#devolviendo True si lo es y False en caso contrario. 
#Escriba un programa principal que lea un número entero del usuario y muestre un mensaje que indique si es primo o no. 
#Asegúrese de que el programa principal no se ejecutará si el archivo que contiene su solución se importa a otro programa.

def Primo (n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def main():
        value = int(input('Introduce un numero entero: '))
        if Primo(value):
            print(value, 'es primo.')
        else:
            print(value,'No es primo')
if __name__ == '__main__':
        main()
