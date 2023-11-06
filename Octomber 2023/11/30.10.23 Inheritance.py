#scope to code the generalized code that can be use in multiple situations
#- to solve a chain of problems
#- helps with eliminating repetition
"""
class people:

    def __init__(self, a, b, c):
        .
        .
        .
        .

    class students (people):

        def ...
    class teachers (people):
    class elder (people):
"""
# a class defines a new datatype (sort of)

class Animal:
    def __init__(self, name):
        self.name = name

    def print_me(self):
        print(f"{self.name}")

myAnimal = []
myAnimal.append(Animal("dog"))
myAnimal.append(Animal("cat"))
myAnimal.append(Animal("snake"))

for animal in myAnimal:
    animal.print_me()


class Animal:
    def __init__(self, name):
        self.name = name

    def print_me(self):
        print (f"{self.name}")

    def speak(self):
        pass

class Mammal(Animal):

    def speak(self):
        pass

class Dog (Mammal):
    def speak(self):
        print(f"{self.name}: Woof Woof")

myDog = Dog("Noora")
myDog.speak()

#doesn't matter if we put mammal or animal as the inheritance class here because they both have the speak function defined the same way
class Cat(Animal):
    def speak(self):
        print(f"{self.name}: Meow Meow")

myCat = Cat("Olli")
myCat.speak()

#Each object belongs to its own class
#Class only preformed behave based on its owen features