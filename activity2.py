class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

class Car(Animal):
    def move(self):
        print("Driving")

class Plane(Animal):
    def move(self):
        print("Flying")

class Dog(Animal):
    def move(self):
        print("Running")

def make_animal_move(animal):
    animal.move()

car = Car()
plane = Plane()
dog = Dog()

make_animal_move(car)
make_animal_move(plane)
make_animal_move(dog)
