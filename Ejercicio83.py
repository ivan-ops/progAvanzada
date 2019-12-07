def envio(productos):
    total = 195 + (productos - 1)*(29.50)
    return total

prod = float(input('cantidad de productos a comprar:'))
env = envio(prod)
print('el costo total del envio es:', env)
