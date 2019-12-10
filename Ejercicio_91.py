# Ejercicio 91
#Escriba una función llamada precedencia que devuelva un número entero que represente la precedencia de un operador matemático. 
#Una cadena que contiene el operador se pasará a la función como su único parámetro. 
#Su función debe devolver 1 para + y -, 2 para * y /, y 3 para ˆ. 
#Si la cadena que se pasa a la función no es uno de estos operadores, la función debería devolver -1. 
#Incluya un programa principal que lea un operador del usuario y muestre la precedencia del operador 
#o un mensaje de error que indique que la entrada no era un operador. 
#Su programa principal solo debe ejecutarse cuando el archivo que contiene su solución no se ha importado a otro programa
def precedence(operation):
    operation = operation.strip()
    if (operation == '+') or (operation == '-'): 
        return 1
    elif (operation == '*') or (operation == '/'): 
        return 2
    elif (operation == '^'):
        return 3
    else: 
        return -1
    
    
def main():    
    op = input("Ingrese el símbolo de la operación que desea evaluar: ")

    result = precedence(op)
    if result == -1: 
        print("El símbolo ingresado no es una operación válida")
    else: 
        print(result)
main()