#Ejercicio 62

print('precio original     | descuento | precio total')
print('----------------------------------------------')


original = 4.95
while original <= 24.95:
    descuento = original * 0.60
    final = original - descuento
    print(' $%.2f''     |' %original, '$%.2f''    |' %descuento, '$%.2f' %final )
    original = original + 5