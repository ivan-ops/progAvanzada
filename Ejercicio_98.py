# Ejercicio 98
#Escriba dos funciones, hex2int e int2hex, que conviertan entre dígitos hexadecimales 
#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F) y enteros de base 10 . 
#La función hex2int es responsable de convertir una cadena que contiene un solo dígito hexadecimal en un entero de base 10, 
#mientras que la función int2hex es responsable de convertir un entero entre 0 y 15 en un solo dígito hexadecimal. 
#Cada función tomará el valor para convertir como su único parámetro y devolverá el valor convertido como el único resultado de la función. 
#Asegúrese de que la función hex2int funcione correctamente para letras mayúsculas y minúsculas. 
#Sus funciones deberían finalizar el programa con un mensaje de error significativo si se proporciona un parámetro no válido.

def hex2int(hexa): 
    H = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    h = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    decimal = 0
    
    while True: 
        for i in hexa:
            if  (i in h) or (i in H):
                continue
            else: 
                print("Acaba de ingresar algo no reconocible como número hexadecimal")
                hexa = input("Ingrese un número en formato hexadecimal: ")
                break
        else: 
            break
    
    for i in range(len(hexa)):
        
        exp = len(hexa) - i -1
        if hexa[i] in h: 
            value = h.index(hexa[i])
        elif hexa[i] in H: 
            value = h.index(hexa[i])
        decimal = decimal + value*16**exp
        
    return decimal 

def int2hex(inter):
    while True: 
        try:
            inter = int(inter)
        except ValueError:
            print("Acaba de ingresar algo no reconocible como número entero")
            inter = input("Ingrese un número positivo entre 0 y 15: ")
            continue
        else:
            inter = int(inter)
            break
    h = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return h[inter]
