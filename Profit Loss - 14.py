cp = int(input("Kindly enter the amount you are scamming the customers for selling your apples:"))
sp = int(input("Kindly enter the amount you are getting scammed by customers for selling your apples at a unbelievable price:"))
if sp > cp:
    print("Oh my god!, You successfully sold your apples at a higher price.GOOD PROFIT!")
elif cp > sp:
    print("Oh man!, well I'll bring a donut to your funeral for the very disturbing loss you made!")
else:
    print("Well well well, That customer forgot to bargain with ya. NO THING")
