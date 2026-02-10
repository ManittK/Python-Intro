try:
    age= int(input("Enter your age: "))
except ValueError:
    print("Enter a number")
except ZeroDivisionError:
    print("It is divisible by 0. Not possible")
finally:
    if age%2==0:
        print("Even Age")
    else:
        print("Odd Age")