class Vehiculo():

    def dezplazamiento(self):
        print("Dezplazamiento")

class Moto(Vehiculo):
    def dezplazamiento(self):
        print("Dezplazamiento de 2 Ruedas")

class Camion(Vehiculo):
    def dezplazamiento(self):
        print("Dezplazamiento de 6 Ruedas")


def dezplamientodevehi(vehiculo):
    vehiculo.dezplazamiento()


vehiculo = Moto()
dezplamientodevehi(vehiculo)

vehiculo = Camion()
dezplamientodevehi(vehiculo)

