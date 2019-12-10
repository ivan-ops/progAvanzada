# Ejercicio 89 
#Muchas personas no usan letras mayúsculas correctamente, 
#especialmente cuando escriben en dispositivos pequeños como teléfonos inteligentes. 
#En este ejercicio, escribirá una función que capitaliza los caracteres apropiados en una cadena. 
#Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y seguida de un espacio. 
#El primer carácter de la cadena también debe estar en mayúscula, 
#así como el primer carácter sin espacio después de un ".", "!" O "?". 
#Por ejemplo, si la función se proporciona con la cadena "¿a qué hora tengo que estar allí? ¿Cuál es la dirección? ", 
#entonces debería devolver la cadena" ¿A qué hora tengo que estar allí? ¿Cuál es la dirección?". 
#Incluya un programa principal que lea una cadena del usuario, la capitalice utilizando su función y muestre el resultado.

def capitilize(s):

    result = s.replace(" i "," I ")
    

    if len(s) > 0:
        print("resultado[0]",result[0])
        result = result[0].upper() + \
        result[1 : len(result)]
        print("escribe con mayúscula el primer carácter de la cadena", result)

    
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            
            pos = pos + 1

            
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1

            
            if pos < len(s):
                result = result[0:pos] + \
                result[pos].upper()+ \
                result[pos+1:len(result)] 
            
        pos = pos + 1

    return result

def main():
    s = input("Introduce el texto: ")
    capitalized = capitilize(s)
    print("Se capitaliza como:", capitalized)


main()
