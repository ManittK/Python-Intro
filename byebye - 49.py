#Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.
active = True

while active:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        while True:
            print("bye")
    else:
        print("Not divisible by 2. Try again.")
