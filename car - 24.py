car = str(input("Please enter your choice as exact words with no space(Bus/Car/Bike)"))
if car == "Bus":
    print("Thank you for your time your bus is booked for tomorrow at 6:30 pm")
else:
    if car == "Car":
        ctype = input("Do you want SUV or SEDAN")
        if ctype == "SUV":
            print("Your SUV has been booked for tomorrow at 6:30 pm")
        elif ctype == "SEDAN":
            print("Your SEDAN has been booked for tomorrow at 6:30 pm")
        else:
            print("Random Car booked :)")
    elif car == "Bike":
        ctype = input("Do you want to scooty or scooter?")
        if ctype == "scooty":
            print("Your scooty bike has been booked for tomorrow at 6:30 pm")
        elif ctype == "scooter":
            print("Your scooter bike has been booked for tomorrow at 6:30 pm")
        else:
            print("Random bike booked :)")
    else:
        print("That is exactly why you should listen to me to avoid such errors!")
