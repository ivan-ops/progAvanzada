def calcular_hipotenusa(lado1 , lado2):
    hipotenusa = (lado1**2 + lado**2)**(0.5)
    return hipotenusa

L1 = float(input('inserta el valor del lado1:'))
L2 = float(input('inserta el valor del lado2:'))
hip1 = calcular_hipotenusa(L1 , L2)
hip2 = calcular_hipotenusa(3.5 , 5.0)
hip2 = calcular_hipotenusa(8.2 , 6.0)
print('la hipotenusa es:',hip1)

