a = int(input("Enter a number ex.12:"))
b = int(input("Enter another number ex.12:"))
c = int(input("Enter last number ex.12:"))

if a and b and c:
    print("All values have boolean value True")
else:
    print({"Any one of the numbers has value of Boolean false"})
    
if a > 5 or b > 5:
    print("a or b looks like is above 5")
else: 
    print("I think c or nothing is a number is above 5")
    