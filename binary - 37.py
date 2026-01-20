decimal = int(input("Enter a decimal number: "))
binary = ""
while decimal > 0:
    rem = decimal % 2
    binary = str(rem) + binary
    decimal = decimal //  2
    print("Binary no now is ", binary)

print("The actual binary is ", binary)
