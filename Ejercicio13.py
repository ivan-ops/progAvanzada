# Ejercicio 13
# Considere el software que se ejecuta en una máquina de autopago. 
# Una tarea que debe ser capaz de realizar es determinar cuánto cambio proporcionar cuando el comprador paga una compra en efectivo.
# Escriba un programa que comience leyendo una cantidad de centavos del usuario como un entero. 
# Luego, su programa debe calcular y mostrar las denominaciones de las monedas que se deben usar para dar esa cantidad de cambio al comprador. 
# Los cambios deben darse usando la menor cantidad de monedas posible. 
# Suponga que la máquina está cargada con monedas de un centavo, cinco centavos, diez centavos, cuartos, loonies y toonies.



centavo = int(input('Introduce los centavos: '))




centa_toon = 200
centa_loon = 100
centa_cuart = 25
centa_diez = 10
centa_cinco = 5
penique = centavo



print('',centavo // centa_toon, 'toonie')
centavo = centavo % centa_toon


print('',centavo // centa_toon, 'loonie')
centavo = centavo % centa_loon


print('',centavo // centa_cuart, 'cuartos')
centavo = centavo % centa_cuart



print('',centavo // centa_diez, 'diez centavos')
centavo = centavo % centa_diez


print('',centavo // centa_cinco, 'cinco centavos')
centavo = centavo % centa_cinco


print('', penique, 'peniques')

