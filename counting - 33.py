
n = int(input("Enter a number: "))
temp = abs(n)
count = 0
while temp > 0:
    temp //= 10  
    count += 1    
    print("Now digits ", count)

print("There are a total of", count, "digits")
