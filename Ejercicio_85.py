#Ejercicio 85
#convertir un entero a un numero cardinal. 
#las palabras como primero segundo tercero y cuarto, son llamados tambien como numeros cardinales
#en este ejercicio debe describir una funcion que tome un numero entero como su unico parametro y regrese una cadena de caracteres.
#con la palabra cardinal del numero entereo insertado.
#su funcion debe manejar los numeros entero entre el 1 y el 12
#y debe regresar su correspondiente en numero cardinal.
#Incluya un programa principal que demuestre su funcion desplegando cada entero del 1 al 12 y su numero cardinal

def cardinal (numero):
    if numero == 1:
        card = 'primero'
    if numero == 2:
        card = 'segundo'
    if numero == 3:
        card = 'tercero'
    if numero == 4:
        card = 'cuarto'
    if numero == 5:
        card = 'quinto'
    if numero == 6:
        card = 'sexto'
    if numero == 7:
        card = 'septimo'
    if numero == 8:
        card = 'octavo'
    if numero == 9:
        card = 'noveno'
    if numero == 10:
        card = 'decimo'
    if numero == 11:
        card = 'onceavo'
    if numero == 12:
        card = 'doceavo'
    return card
entero = int(input('Inserte el numero entero: '))

num= cardinal(entero) 
print('la numero entero en cardinal es: ',num)