def tarifa(distancia):
    total = 44.00 + distancia*12.00
    return total

dist = float(input('inserta la distancia manejada (KM):'))
cuota = tarifa(dist)
print('el costo del viaje es:', cuota)