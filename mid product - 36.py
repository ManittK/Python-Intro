num = input("Enter a high number:")
length = len(num)
if length%2==0:
    mid1 = int(num[length // 2 - 1])
    mid2 = int(num[length //2])
    product = mid1 * mid2
    print("Mid product is ", product)
else:
    mid = int(num[length // 2])
    product = mid
    print("Mid product is ", product)
