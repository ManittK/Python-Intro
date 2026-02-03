def tc(b, tp):
    ttl = b*(1 + 0.01*tp)
    ttl = round(ttl, 2)
    print(f"Please pay ${ttl}")

b = int(input("Enter the bill amount: "))
tp = int(input("Enter the tip percent: "))
tc(b, tp)