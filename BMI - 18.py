height = int(input("Please enter your height in cm:"))
weight = int(input("Please enter your weight in kg:"))
BMI = weight / (height/100) ** 2
print("You have BMI as ", BMI)
if BMI <= 18.4:
    print("You are Underweight")
elif BMI <= 24.9:
    print("You are Healthy :)")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severly over weight")
elif BMI <= 39.9:
    print("You are Obese")
else:
    print("You are severly Obese")