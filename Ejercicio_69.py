# Ejercicio 69
# El valor de π se puede aproximar mediante las siguientes series infinitas:

# Escriba un programa que muestre 15 aproximaciones de π. 
# La primera aproximación debe utilizar solo el primer término de la serie infinita. 
# Cada aproximación adicional mostrada por su programa debe incluir un término más en la serie, 
# por lo que es una mejor aproximación de π que cualquiera de las aproximaciones mostradas anteriormente.
j = 0
i = 1
suma = 0.0
signo = -1
while i <= 30:
    den = (i+1.0)*(i+2.0)*(i+3.0)
    signo = signo * -1
    suma = suma + (signo * 4.0 / den)
    i=i+2.0
    pi_ap = 3.0 + suma
    j = j+1
    print('Iteracion: ', j, 'Pi Aprox', pi_ap)
    

