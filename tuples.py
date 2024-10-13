

numbers=(1,2,3)
#numbers[1]=1
print(numbers)

#Unpacking

coordinates=(1, 2, 3)
# x=coordinates[0]
# y=coordinates[1]
# z=coordinates[2]
#we can achieve the same result ny unpacking
x,y,z=coordinates
print(x,y,z)
#we can also use unpacking with list

#Dictonaries or key value pairs
customer={
    "name":"John smith",
    "age":30,
    "is_verified":True
}
print(customer["name"])
#print(customer[birthdate]) #unsafe, this will show error
print(customer.get("name")) #safe
print(customer.get("birthdate", "Dec 1 1990"))
customer["salary"]=34000
print(customer)

#exercise

phone=input("Phone: ")
digits_mapping={
    "1":"One",
    "2":"Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output= ""
for char in phone:
    output+= digits_mapping.get(char, "!") + " "
print(output)

#Emoji Converter

messages=input("> ")
words=messages.split(" ") #split the words based on space.
emojis={
    ":)":"😀",
    "):":"😔"
}
ans=""
for word in words:
    ans+=emojis.get(word,word)+" "
print(ans)

