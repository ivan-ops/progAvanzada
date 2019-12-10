# Ejercicio 93
#En este ejercicio creará una función llamada nextPrime que encuentra y 
#devuelve el primer número primo mayor que algún entero, n. 
#El valor de n se pasará a la función como su único parámetro. 
#Incluya un programa principal que lea un número entero del usuario y 
#muestre el primer número primo mayor que el valor ingresado. 
#Importe y use su solución para el Ejercicio 92 mientras completa este ejercicio.
def nextPrime(n):
    while True: 
        if n < 0: 
            print("www")
            print("El número no es un entero positivo")
            n = float(input("Ingrese un número entero positivo: "))
        elif n != int(n): 
            print("El número no es un entero positivo")
            n = float(input("Ingrese un número entero positivo: "))
        else: 
            break
    n = int(n)
    n = n+1
    while True:
        for i in range(2,n): 
            if n%i == 0: 
                n = n+1
                break
        else: 
            print("El primero primo más grande que el número ingresado es: ", n)
            break

def main():
    number = float(input("Ingrese un número entero positivo: "))
    nextPrime(number)

main()
