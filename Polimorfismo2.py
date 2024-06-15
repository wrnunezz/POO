#POlimorfirmo
class Vehiculo:

    def dezplazamiento(self):
        print("Dezplazamiento de 4 Ruedas")

class Moto(Vehiculo):
    def dezplazamiento(self):
        print("Dezplazamiento de con 2 ruedas")
class Camion(Vehiculo):
    def dezplazamiento(self):
        print("Dezplazaminto con 6 ruedas")


def dezplazamientodeVehiculos(vehiculo):
    vehiculo.dezplazamiento()

vehiculo = Moto()
dezplazamientodeVehiculos(vehiculo)
vehiculo = Camion()
dezplazamientodeVehiculos(vehiculo)
