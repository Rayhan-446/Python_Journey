"""
is_hot=False
is_cold=True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
"""
from ctypes import c_char

"""
price=1000000
has_good_credit=False
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down payment: ${down_payment}")
"""
"""
has_high_income=True
has_good_credit=False
has_criminal_record=False

if has_high_income or has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else: print("Not Eligible")
"""

temperature=35
if temperature!=30:
    print("It's not a hot day")
else: print("It's either hot or cold day")

#exercise1
name=str(input("Enter your name : "))
if len(name)<3:
    print(f"Name has {len(name)} characters which must be at least 3 characters")
elif len(name)>50:
    print(f"Name has {len(name)} characters which can be a maximum of 50 characters")
else: print("Name looks good!")
#exercise2
weight=int(input("Weight: "))
option=str(input("(L)bs or (K)g: "))
if option=='l' or option== 'L': #option.upper()=="L":
    print(f"You are {weight*0.45} kg")
else: print(f"You are {weight/0.45} pounds")
