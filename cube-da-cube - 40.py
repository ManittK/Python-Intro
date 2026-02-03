def cuhbe(num):
    cube = num **3
    return cube
num = int(input("Enter a random number: "))
if num%3==0:
    print("The cube of the number is ", cuhbe(num))
else:
    print("System Error")