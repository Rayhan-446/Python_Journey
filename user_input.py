'''
name=input("What's your name? ")

color=input("What's your favourite color? ")
print(name+" likes "+color)
age=int(input("Enter your age = "))
'''
from pyexpat.errors import messages

name=input()
last=input()
# print(name[-1],name[0],name[-2])
# print(name[0:3])
# print(name[2:])
# print(name[0:])
# print(name[:4])
# another=name[:]
# print(another)
# print(name[1:-1])
"formated strings"
message=name+' ['+last+'] is a coder'
print(message)
#formated text
msg=f'{name} [{last}] is a coder'
print(msg)
print(len(msg))
print(msg.upper())
print(msg.lower())
print(msg.find('p')) #It'll show the 1st occurrence index of the char in this string
print((msg.find('is')))
print(msg.replace('Rayhanp','Rayhan')) #Replace a string
print('Rayhan' in msg) #it's a boolean


