# Escriba un programa que lea un numero entero por el usuario.
# Su programa debe despleglar un mensaje indicando si su numero entero es par o impar


numero = int(input('Introduzca un numero entero: '))



if (numero%2==0):
    print(str(numero)+' es par')
else:
    print(str(numero)+' es impar')
