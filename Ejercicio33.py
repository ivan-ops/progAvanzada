# Ejercicio 33

# Una panadería vende hogazas de pan por $ 3.49 cada una. 
# El pan de un día tiene un descuento del 60 por ciento. 
# Escriba un programa que comience leyendo la cantidad de hogazas de pan de un día compradas al usuario. 
# Luego, su programa debe mostrar el precio regular del pan, el descuento porque tiene un día de antigüedad y el precio total. 
# Todos los valores deben mostrarse usando dos decimales
# los puntos decimales en todos los números deben alinearse cuando el usuario ingresa valores razonables.



undia = int(input("Introduce la cantidad de pan que comprara: "))



regular = undia * 3.49
preciodes = undia * (3.49 * 0.60)


total = regular - preciodes



print("El precio normal es:      $%5.2f" %(regular))
print("El descuento de un dia:   $%5.2f" %(preciodes))
print("El total a pagar es:      $%5.2f" %(total))