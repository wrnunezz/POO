#
#
#
from abc import ABC, abstractmethod

class Pieza(ABC):
    def __init__(self, color, posicion):
        self.color = color
        self.posicion = posicion

    @abstractmethod
    def mover(self, nueva_posicion):
        # Método abstracto que debe ser implementado por las clases derivadas
        pass

# Clase derivada Torre que hereda de Pieza
class Torre(Pieza):
    def mover(self, nueva_posicion):
        # Lógica específica para mover una torre en ajedrez
        print(f"Torre movida de {self.posicion} a {nueva_posicion}")
        self.posicion = nueva_posicion

# Clase derivada Alfil que hereda de Pieza
class Alfil(Pieza):
    def mover(self, nueva_posicion):
        # Lógica específica para mover un alfil en ajedrez
        print(f"Alfil movido de {self.posicion} a {nueva_posicion}")
        self.posicion = nueva_posicion

# Crear instancias de Torre y Alfil
torre = Torre("blanco", "a1")
alfil = Alfil("negro", "c1")

# Mover las piezas
torre.mover("a4") # Output: Torre movida de a1 a a4
alfil.mover("h6") # Output: Alfil movido de c1 a h6