#Ejercicio 32

# Cree un programa que lea tres enteros del usuario y los muestre en orden, ordenado (de menor a mayor). 
# Use las funciones min y max para encontrar los valores más pequeños y más grandes. 
# El valor medio se puede encontrar calculando la suma de los tres valores y luego restando el valor mínimo y el valor máximo.



uno = int(input("Introduce el primer numero: "))
dos = int(input("Introduce el segundo numero: "))
tres = int(input("Introduce el tercer numero: "))


menor = min(uno, dos, tres)
mayor = max(uno, dos, tres)
medio = (uno+dos+tres) - menor - mayor


print("\n El orden de menor a mayor es: " ,menor, ',', medio, ',', mayor)
