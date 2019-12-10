# Ejercicio 95
#En una jurisdicción particular, las matrículas más antiguas consisten en tres letras seguidas de tres números. 
#Cuando se utilizaron todas las placas que siguen ese patrón, el formato se cambió a cuatro números seguidos de tres letras.
#Escriba una función que genere una matrícula aleatoria. 
#Su función debe tener una probabilidad aproximadamente igual de generar una secuencia de caracteres para una placa anterior o una nueva. 
#Escriba un programa principal que llame a su función y muestre la placa generada al azar.

import random as rand



def license_gen():
    set_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    set_numbers = [1,2,3,4,5,6,7,8,9,0]
    lenght = rand.randint(3,4)
    licen_numbs = rand.sample(set_numbers,lenght)
    licen_letts = rand.sample(set_letters,3)
    licen = ''
    if lenght == 3: 
        for i in licen_letts:
            licen = licen + i
        for i in licen_numbs: 
            licen = licen + str(i)
    elif lenght == 4: 
        for i in licen_numbs:
            licen = licen + str(i)
        for i in licen_letts: 
            licen = licen + i    
    print(licen)
    return licen

def main():
    license_gen()

main()  