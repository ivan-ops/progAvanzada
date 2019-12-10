# Ejercicio 96
#En este ejercicio escribirá una función que determina si una contraseña es buena o no. 
#Definiremos una buena contraseña para que tenga una longitud de al menos 8 caracteres y contenga al menos una letra mayúscula, 
#al menos una letra minúscula y al menos un número. Su función debe devolver verdadero si la contraseña que se le pasó, 
#ya que su único parámetro es bueno. De lo contrario, debería devolver falso. 
#Incluya un programa principal que lea una contraseña del usuario e informe si es buena o no. 
#Asegúrese de que su programa principal solo se ejecute cuando su solución no se haya importado a otro archivo.
def checkPassword(password): 
    has_upper = False
    has_lower = False
    has_num = False
    
    for ch in password: 
        if ch >= 'A' and ch <= 'Z': 
            has_upper = True
        elif ch >= 'a' and ch <= 'z': 
            has_lower = True
        elif ch >= '0' and ch <= '9':    
            has_num = True
    
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False

def main(): 
    p = input("Ingrese Contraseña: " )
    if checkPassword(p): 
        print("La contraseña es buena")
    else: 
        print("La contraseña es débil")

if __name__ == "__main__": 
    main()
