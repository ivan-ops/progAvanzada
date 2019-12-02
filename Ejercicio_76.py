# Ejercicio 76
#La factorización prima de un número entero, n, se puede determinar utilizando los siguientes pasos: Inicializar factor a dos
# while el factor es menor o igual que n do
# if n es divisible uniformemente por factor, then
# Concluir que el factor es un factor de n
# Divide n por factor usando la división entera
# else
# Aumenta el factor en uno
#Escriba un programa que lea un número entero del usuario. 
#Si el valor ingresado por el usuario es menor que 2, entonces su programa debería mostrar un mensaje de error apropiado.
#De lo contrario, su programa debería mostrar los números primos que se pueden multiplicar para calcular n, 
#con un factor que aparece en cada línea. 

def wrong_input_handling(data):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número")
            data = input("Ingrese un entero positivo: ")
            continue
        if data < 0:
            print("Su número es negativo. No se acepta")
            data = input("Ingrese un entero positivo: ")
            continue
        elif data != int(data):
            print("Su número es decimal. No se acepta")
            data = input("Ingrese un entero positivo: ")
            continue
        else:
            data = int(data)
            break
        
    return data

def prime_factorization(n):
    n = wrong_input_handling(n)
    factor = 2
    
    while factor <= n: 
        if n%factor == 0:
            print(factor)
            n = n//factor
        else: 
            factor = factor +1

number = input("Ingrese el número que desea factorizar: ")

print(prime_factorization(number))
none