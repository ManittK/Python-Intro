medic = str(input("Enter if you have/not have medical cause(Y/N):"))
attend = int(input("Enter your atendance out of 212:"))

if medic == "Y":
    print("Allowed")
else:
    if attend >= 75:
        print("Allowed")
    else:
        print("Not Allowed")