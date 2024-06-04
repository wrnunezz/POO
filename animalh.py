class Animal:
    def __init__(self, sonido):
        self.sonido = sonido

    def hacer_sonar(self):
        print(self.sonido)


# Clase hija Perro que hereda de Animal
class Perro(Animal):
    def __init__(self):
        # Llama al constructor de la clase
        super().__init__("Guauuuuu!")


# Clase hija Gato que hereda de Animal
class Gato(Animal):
    def __init__(self):
        # Llama al constructor de la clase base
        super().__init__("Miau!")


# Crear instancias de Perro y Gato
perro = Perro()
gato = Gato()

# Usar el método hacer_sonar heredado de la clase Animal
perro.hacer_sonar()  # Output: 
gato.hacer_sonar()  # Output: