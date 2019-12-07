class Cuenta:
    def __init__(self,monto):
        self.monto = monto


    def depositar(self, cantidad):
        self.monto = self.monto + cantidad
        print('Depositaste:', cantidad, 'Tu saldo es:', self.monto)

    def retirar(self, cantidad):
        self.monto = self.monto - cantidad
        print('Retiraste', cantidad, 'Tu saldo es:', self.monto)




cuenta_francisca = Cuenta(100)
cuenta_francisca.depositar(2000)
cuenta_francisca.retirar(300)

cuenta_ivan = Cuenta(100)
cuenta_ivan.retirar(90)