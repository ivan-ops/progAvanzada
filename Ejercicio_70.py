# Ejercicio 70
# uno de los primeros ejemplos de encriptacion fue usado por julio cesar.
# Julio cesar necesitaba el enviar instrucciones escritas a sus generales,
# Pero el no queria que sus enemigos conocieran de sus planes en caso de que el mensaje fuese interceptado.
# Como resultado el desarrollo lo que despues seria conocido el sifrado de cesar.
# La idea detras de este cifrado es simple.
# y como resultado no tiene porteccion contra las tecnicas modernas de jaqueo.
# Cada letra en el mensaje original se mueve tres lugares. 
# como resultado A se convierte en D, B se convierte en E, C se converte en F, D se convierte en G, etc.
# Las ultimas tres letras del alfabeto se mueven al inicio es decir,
# X se convierte en A, Y se convierte en B, Z se convierte en C.
# Escriba un programa que implemente el cifrado cesar.
# Permita que el usuario inserte el mensaje y la cantidad de espacios a moverse,
# Y despues despliege el mensaje movido.
# Su programa debe de soportar letras mayusculas y minusculas.
# Su programa tambien debe soportar movimientos con valor negativos, de tal manera que los mensajes se puedan cifrar y desifrar

frase = input('Introduce el mensaje: ')
movimiento = int(input('Introduce movimiento: '))

nfrase = ''

for ch in frase:
    if ch >= 'a' and ch <='z':
        pos = ord(ch) - ord('a')
        pos = (pos + movimiento) % 26
        caracter = chr (pos + ord ('a'))
        nfrase = nfrase + caracter
    elif ch >'A' and ch <= 'Z':
        pos = ord(ch) - ord ('A')
        pos = (pos + movimiento) % 26
        caracter = chr(pos + ord('A'))
        nfrase = nfrase + caracter
    else:
        nfrase = nfrase + ch
print('El mensaje cifrado es: ', nfrase)