# Polimorfismo: El polimorfismo es la capacidad de objetos de diferentes clases de responder a un mismo mensaje de diferentes formas.
# En Python, el polimorfismo se logra a través de la implementación de métodos con el mismo nombre en diferentes clases.
# Cada clase puede tener su propia implementación del método, pero se llama al método adecuado según el tipo de objeto con el que se esté trabajando.

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau!")

class Gato(Animal):
    def sonido(self):
        print("Miau!")

def hacer_sonar(animal):
    # Llamamos al método sonido del objeto pasado como parámetro,
    # sin importar de qué clase específica es. Esto es polimorfismo.
    animal.sonido()

perro = Perro()
gato = Gato()

hacer_sonar(perro) # Output: "Guau!"
hacer_sonar(gato) # Output: "Miau!"