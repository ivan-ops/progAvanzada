class Gelatina:
    def __init__(self,color,sabor):
        self.color=color
        self.sabor=sabor
    def desplegar_info(self):
        print('Mi color es: ',self.color,'y mi sabor es: ',self.sabor)

gelatina1 = Gelatina('rojo','grosella')
gelatina2 = Gelatina('verde' ,'limon')
gelatina3 = Gelatina('morado','uva')

gelatina1.desplegar_info()
gelatina2.desplegar_info()
gelatina3.desplegar_info()

#Escribir una clase llamada estudiante que obedesca el siguiente diagrama UML

class Estudiante:
    def __init__(self,nombre,matricula,creditos):
        self.nombre = nombre
        self.matricula = matricula
        self.creditos = creditos
    def desplegar_info(self):
        print('Nombre del estudiante:',self.nombre,'     Matricula:',self.matricula,'     No de creditos:',self.creditos)

estudiante1 = Estudiante('Ivan','15090437','3')
estudiante2 = Estudiante('Neopolo','15090452','6')
estudiante3 = Estudiante('Ivaan','15090427','4')
estudiante4 = Estudiante('Jhonatan','16090613','2')
estudiante5 = Estudiante('Juan','15090450','5')


estudiante1.desplegar_info()
estudiante2.desplegar_info()
estudiante3.desplegar_info()
estudiante4.desplegar_info()
estudiante5.desplegar_info()

