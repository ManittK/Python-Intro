
bill = float(input("Enter total bill: "))
paid = float(input("Enter amount paid: "))

balance = bill - paid

if balance > 0:
    print(f"Customer still owes: $", balance)
elif balance < 0:
    print(f"Give back change: $", abs(balance))
else:
    print("Bill is paid in full!")
