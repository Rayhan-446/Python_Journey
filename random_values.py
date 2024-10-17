#list of built-in modules
#https://docs.python.org/3/py-modindex.html
import random

# for i in range(3):
#     print(random.random())

# for i in range(10):
#     print(random.randint(0,10))

# members=['John','Bob','Mary','Steve','Rayhan']
# leader=random.choice(members)
# print(leader)

class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second  #they are tuple

dice=Dice()
print(dice.roll())