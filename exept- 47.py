#Write a program to understand how the value error exception works?
try:
    num = int(input("Enter a random number: "))
    print("The number you gave was ", num)
except ValueError as ex:
    print("Exception: ", ex)