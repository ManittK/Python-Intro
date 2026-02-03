def f(x):

    if x == 0 or x == 1:
        return 1
    else:
        return x*f(x-1)
    
x = int(input("Enter a number for its factorial: "))
print("This is the factorial of ", x,": ", f(x))