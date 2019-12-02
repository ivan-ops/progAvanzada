#Ejercicio 81
#Eescribir una funcion que tome la longitud de los dos lados mas cortos de un triangulo rectangulo como argumentos.
#La funcion debe de regresar la hipotenusa del triangulo calculado usando el teorema de pitagoras como resultado.

#Incluya un programa principal que lea las longitudes de los lados mas cortos de un tringulo rectangulo insertados por el usuario.
#Usando la funcion para calcular la longiutd de la hipotenusa y que tambien se despliege el resultado.

def calcular_hipotenusa (lado1,lado2):
    hipotenusa = (lado1**2 + lado2**2)**(0.5)
    return hipotenusa
L1 = float(input('inserta el lado 1: '))
L2 = float(input('inserta el lado 2: '))

hip = calcular_hipotenusa(L1,L2)
hip2 = calcular_hipotenusa(3.5,5.0)
print('La hipotenusa es: ', hip)
print('La hipotenusa es: ', hip2)