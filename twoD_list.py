"""matrix=[
    [1,2,4],
    [2,4,3],
    [5,3,1]
]
matrix[0][2]=10
print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)
print(matrix)"""
from enum import unique

#from Python_Journey.for_loops import number

#List methods
numbers=[5,2,1,7,4,2,1]
"""numbers.append(20)
print(numbers)
numbers.insert(0,7)
print(numbers)
numbers.remove(7)
print(numbers)
numbers.remove(7)
print(numbers)
#numbers.clear()
print(numbers)
print(numbers.pop()) #delete from the last index
print(numbers)
print(numbers.index(2)) #not safe coz it shows error if it doesn't occur.
print(50 in numbers) #safe
print(numbers.count(2))
#print(sorted(numbers)) # it will just show sorted list but don't change, actually.
print(numbers.sort())
print(numbers)
numbers.reverse()
print(numbers)
numbers2=numbers.copy()
"""
#write a program to remove the duplicates in a list.
uniques=[]
for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)


