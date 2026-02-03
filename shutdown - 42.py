def sd(m):
    if m == "wood":
        return "Ten trees cut 50 pieces of wood is at your doorstep!"
    elif m == "cotton":
        return "Extracted cotton, 1 kg of cotton now at your doorstep!"
    
m = str(input("What are you shortage one?(wood/cotton):  "))
print(sd(m))