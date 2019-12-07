class Triangulo:
    def __init__ (self,angulo1,angulo2,angulo3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3
    def checar_angulos(self):
        suma = self.angulo1+self.angulo2+self.angulo3
        if suma == 180:
            print('True')
        else:
            print('False')

mi_triangulo= Triangulo(90,30,60)
mi_triangulo2= Triangulo(90,90,70)

mi_triangulo.checar_angulos()

mi_triangulo2.checar_angulos()


