# for item in "Python":
#     print(item)
# for item in ["Rayhan","Riyad","Rana"]:
#     print(item)
# for it in [3,4,5,6,3]:
#     print(it)
# for item in range(5,12,2):
#     print(item)
"""prices=[10,20,30]
total_price=0
for item in prices:
    total_price+=item
print(total_price)"""

#Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

number=[5,2,5,2,2]
# for x in number:
#     print('x'*x)

for x in number:
    output=''
    for y in range(x):
        output+='x'
    print(output)

#Lists
names=['john','bob','mosh','sarah','mary']
names[0]='jon'
print(names[2:4])
print(names)

#exercise Largest number on list
listi=[3,4,8,7,0,8]
maxi=listi[0]
for item in listi:
    if item>maxi:
        maxi=item
print(maxi)
print(min(listi))
print(max(listi))



