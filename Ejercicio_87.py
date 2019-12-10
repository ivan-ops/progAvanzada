# Ejercicio 87
#Escriba una función que tome una cadena de caracteres como su primer parámetro, 
#y el ancho de la terminal en caracteres como su segundo parámetro. 
#Su función debe devolver una nueva cadena que consta de la cadena original y el número correcto de espacios iniciales 
#para que la cadena original aparezca centrada dentro del ancho proporcionado cuando se imprima. 
#No agregue ningún carácter al final de la cadena. Incluya un programa principal que demuestre su función.

WIDTH = 80

def centro(s, width):
    if width < len(s):
        return s
    
    espacios = (width - len(s)) // 2
    resultado = ' ' * espacios + s

    return resultado

def main():
    print(centro(' una fabulosa historia', WIDTH))
    print(centro('por: ', WIDTH))
    print(centro('algunos famosos', WIDTH))
    print()
    print('Una vez en el timpo...')
main()