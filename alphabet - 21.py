alpha = input("Enter a random value:")
if alpha == type(str) or alpha == type(bool):
    print("Yes this is a alphabet or a sentence or a boolean")
elif alpha == type(int) or alpha == type(float):
    print("OH No it is a number or a decimal")
else:
    print("Not a functional value")