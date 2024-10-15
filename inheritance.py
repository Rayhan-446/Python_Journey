class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    pass

dog=Dog()
dog.bark()
dog.walk()
cat=Cat()
cat.walk()