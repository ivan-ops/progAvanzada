#Ejercicio 56
#Un plan particular de telefonía celular incluye 50 minutos de tiempo al aire y 50 mensajes de texto por $ 15.00 al mes. 
#Cada minuto adicional de tiempo de emisión cuesta $ 0.25, mientras que los mensajes de texto adicionales cuestan $ 0.15 cada uno. 
#Todas las facturas de teléfonos celulares incluyen un cargo adicional de $ 0.44 
#para respaldar los centros de atención telefónica del 911, y toda la factura (incluido el cargo del 911) 
#está sujeta al impuesto sobre las ventas del 5 por ciento.
#Escriba un programa que lea la cantidad de minutos y mensajes de texto utilizados en un mes por parte del usuario. 
#Muestre el cargo base, el cargo adicional por minutos (si corresponde), 
#el cargo adicional por mensaje de texto (si corresponde), la tarifa del 911, el impuesto y el monto total de la factura. 
#Solo muestre los cargos adicionales por minutos y mensajes de texto si el usuario incurrió en costos en estas categorías. 
#Asegúrese de que todos los cargos se muestren con 2 decimales.

minutos = int(input("Introduce el numero de minutos: "))
mensajes = int(input("Introduce el numero de mensajes de texto: "))

base = 15.00
print('\n Cargo base: $%.2f'%base,)

if minutos >50:
    min = minutos-50
    add_min = min *0.15
    print('\n costo adicional por minutos: $%.2f' %add_min)
elif minutos:
    add_min = 0 


if mensajes >50:
    minu = mensajes-50
    add_men = minu * 0.25
    print('\n costo adicional por mensajes: $%.2f'%add_men)
elif mensajes:
    add_men = 0 


cargo = 0.44
print('\n Cargo del 911: $%.2f'%cargo)

subtotal = base+add_min+add_men+cargo

impuesto = subtotal * 0.5
print('\n El impuesto es: $%.2f'%impuesto)

total= subtotal+impuesto
print('\n Total: $%.2f'%total)

© 2019 GitHub, Inc.