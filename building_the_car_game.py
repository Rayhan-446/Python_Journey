command=""
started=0
while True:
    command=input("> ").lower()
    if command=="start":
        if started==1:
            print("The car is already running")
        else:
            print("Car started.....")
            started=1
    elif command=="stop":
        if started==0:
            print("The car is already stopped")
        else:
            print("Car stopped.")
            started=0
    elif command=="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command=="quit":
        break
    else:
        print("Sorry, I don't understand that!")

