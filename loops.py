"""
i=1
while i<=5:
    print('*'*i)
    i+=1
print("Done")
"""
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count+=1
    if guess==secret_number:
        print("You won!")
        break
else: #similar to the if statement while loop also have else part
    print("Sorry, you failed!")



