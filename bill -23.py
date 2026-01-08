unit = int(input("Enter the amount of units you ahve used this month or else Balck PAnther would come in your Kitchen and steal your food:"))
if unit < 50:
    price = (2.60*unit) + 25
    print("This is your bill for the month: ", price)
else:
    if unit >= 50 and unit < 100:
        price = (3.25*unit) + 35
        print("This is your bill for the month: ", price)
    elif unit >= 100 and unit < 200:
        price = (5.26*unit) + 45
        print("This is your bill for the month: ", price)
    else:
        price = (8.45*unit) + 75
        print("This is your bill for the month: ", price)
