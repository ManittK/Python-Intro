n = 0
i = 0
count = int(input("Enter a random number to count to:"))
while i == 0:
    print("So far this loop has been going on for ", n," times")
    n+=1
    count-=1
    if count == 0:
        print("Let's now stop")
        i = 1



