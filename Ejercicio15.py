# Ejercicio 15
# En este ejercicio, creará un programa que comienza leyendo una medida en pies del usuario. 
# Luego, su programa debe mostrar la distancia equivalente en pulgadas, yardas y millas. 
# Use Internet para buscar los factores de conversión necesarios si no los tiene memorizados.


pies = int(input('Introduce la distancia en pies: '))


millas = pies * 0.000189
yardas = pies * 0.333333
pulgadas = pies * 12



print("\n En millas:    %.6f."   %(millas))
print("\n En yardas:    %.6f."   %(yardas))
print("\n En pulgadas: %.6f." %(pulgadas))