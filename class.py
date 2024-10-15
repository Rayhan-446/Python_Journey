class Point:
    def __init__(self): #constructor
        self.x=0
        self.y=0

    def move(self):
        print("moved")
    def draw(self):
        print("drawn")
point1 = Point()
point1.move()
point1.x=10
print(point1.x)
print(point1.y)

#exercise
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

John=Person("John")
John.talk()
Bob=Person("Bob")
Bob.talk()


