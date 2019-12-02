# Ejercicio 77
#Escriba un programa que convierta un número binario (base 2) a decimal (base 10). 
#Su programa debe comenzar leyendo el número binario del usuario como una cadena. 
#Luego, debe calcular el número decimal equivalente procesando cada dígito en el número binario. 
#Finalmente, su programa debe mostrar el número decimal equivalente con un mensaje apropiado.

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)): 
        decimal = decimal + int(binary[i])* 2**(len(binary)- i - 1)
    return decimal


binary = input("Ingrese el número binario que desea convertir: ")

i = 0
while i < len(binary): 
    if (binary[i] != "0") and (binary[i] != "1"):
        print("El valor ingresado no es un número binario")
        binary = input("Ingrese el número binario que desea convertir: ")
        i = 0
    else: 
        i = i+1

print(binary_to_decimal(binary))
