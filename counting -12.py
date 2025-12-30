amount = int(input(" Kindly enter the amount needed to withdraw:"))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print("Here is the notes of 100 x", note_1)
print("Here is the notes of 50 x", note_2)
print("Here is the notes of 10 x", note_3)