# Ejercicio 30

# En este ejercicio creará un programa que lee la presión del usuario en kilopascales. 
# Una vez que se haya leído la presión, 
# su programa debe informar la presión equivalente en libras por pulgada cuadrada, milímetros de mercurio y atmósferas. 
# Usa tus habilidades de investigación para determinar los factores de conversión entre estas unidades


kiloPascal = float(input('Introduce la presion en kilo-pascales: '))


PSI = kiloPascal * 0.145037738
mercurio = kiloPascal * 7.50062
atm = kiloPascal / 101.3



print('\n En Libras por pulgada^2:        %.3f'%(PSI),'(PSI)')
print('\n En Millimetros de Mercury:    %.3f'%(mercurio),'(mmHg)')
print('\n En Atmosferas:                   %.3f'%(atm),'(atm)')
