#Write a program to check how the exceptions and finally statement works
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error 11")
except SyntaxError:
    print("Comma is missing.")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")