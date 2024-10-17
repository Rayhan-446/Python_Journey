"""def greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")


print("Start")
greet_user("Rayhan","Rimon") #position arguments
#greet_user("Mary")
print("Finish")

#Keyword Arguments where position doesn't really matters
greet_user(last_name="Tuhin",first_name="Arafat")
"""
from re import split



#Return Statement
"""
def square(n):
    return n*n

val=int(input())
res=square(val)
print(res) #print(square(val))"""

def emoji_converter(message):
    words=message.split(" ")
    emojis={
        ":)":"😀",
        "):":"😔"
    }
    output=""
    for word in words:
        output+=emojis.get(word,word)+" "
    return output

# message=input("> ")
# print(emoji_converter(message))
