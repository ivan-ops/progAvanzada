# Ejercicio 80
#¿Cuál es el número mínimo de veces que tiene que lanzar una moneda antes de poder 
#tener tres lanzamientos consecutivos que den como resultado el mismo resultado (o los tres son sol o los tres son cruz? 
#¿Cuál es el número máximo de volteos que podrían ser necesarios? ¿Cuántas vueltas se necesitan en promedio? 
#En este ejercicio exploraremos estas preguntas creando un programa que simule varias series de lanzamientos de monedas.
#Cree un programa que use el generador de números aleatorios de Python para simular lanzar una moneda varias veces. 
#La moneda simulada debe ser justa, lo que significa que la probabilidad de sol es igual a la probabilidad de cruz. 
#Su programa debe voltear monedas simuladas hasta que ocurran 3 sol consecutivas de 3 cruz consecutivas. 
#Muestre una S cada vez que el resultado sea sol, y una C cada vez que el resultado sea cruz, 
#con todos los resultados mostrados en la misma línea. 
#Luego muestre el número de vueltas necesarias para alcanzar 3 vueltas consecutivas con el mismo resultado. 
#Cuando se ejecuta su programa, debe realizar la simulación 10 veces e informar el número promedio de vueltas necesarias.
#La salida de muestra se muestra a continuación:

import random



def coin_flipper():
    
    opcion = ['S', 'C']
    vueltas = ''
    
    while True:
        vuelta = random.choice(opcion)
        vueltas = vueltas + vuelta
        
        if len(vueltas) >= 3:
            if ( vueltas[-3] == vueltas[-2] == vueltas[-1] ):
                break
            else:
                continue
    return vueltas




resultado = []
suma = 0

for i in range(10):
    resultado.append(coin_flipper())
    suma += len(resultado[i])
    print(resultado[i], "(%d)" %len(resultado[i]))

vueltasprom = suma/10    

print ("En promedio %d vueltas" %vueltasprom)
