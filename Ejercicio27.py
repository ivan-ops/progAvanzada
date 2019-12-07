# Ejercicio 27

# calculadora de IMC
# Escriba un programa que calcule el índice de masa corporal (IMC) de un individuo. 
# Su programa debe comenzar leyendo una altura y un peso del usuario. Utilizando la siguiente formula:
# IMC = masa/peso^2



masa = float(input('inserte su masa en KG: '))
estatura = float(input('inserte su estatura en metros: '))



imc = masa / estatura**2

if imc< 16 : 
    print ('Tiene delgadez severa')
elif imc >= 16 and imc < 17:
    print('Tiene delgadez moderada')
elif imc >= 17 and imc < 18.5:
    print('Tiene delgadez leve')
elif imc >= 18.5 and imc < 25:
    print('Tiene estado normal')
elif imc >= 25 and imc < 30:
    print('Tiene preobesidad')
elif imc >= 30 and imc < 35:
    print('Tiene obesidad leve')
elif imc >=35 and imc < 40:
    print('Tiene obesidad media')
elif imc >= 40:
    print('Tiene obesidad morbida')
else :
    print('Los datos no son correctos')
print('Su imc fue de', imc)