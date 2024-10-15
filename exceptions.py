try:
    age=int(input("Age : "))
    print(age)
    income=2000
    risk=income/age
except ZeroDivisionError :
    print("Age cannot be zero")
except ValueError :
    print("Invalid Input")