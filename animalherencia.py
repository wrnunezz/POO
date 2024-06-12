class Animal:
    def __init__(self, name,peso):
        self.name = name
        self.peso = peso

    def eat(self):
        self.peso += 1


class Dog(Animal):
    def __init__(self, name,peso,ladrido):
        super().__init__(name,peso)
        self.ladrido = ladrido

class Cat(Animal):
    def __init__(self, name,peso,maulla):
        super().__init__(name,peso)
        self.maulla = maulla

#creacmos instancias de los objetos
dog = Dog("Peluchin",5,5)
cat = Cat("Negro",6,5)
dog.eat()
print(dog.peso)
#print(dog.ladrido)



