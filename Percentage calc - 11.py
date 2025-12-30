print("Kindly enter your marks of the recent examinatioon or else i will deduct 20 marks from 0 marks:")
maths = int(input("Enter the marks of maths:"))
science = int(input("Enter the marks of science:"))
hindi = int(input("Enter the marks of hindi:"))
english = int(input("Enter the marks of english:"))
sum = maths + science + hindi + english
Pmarks = (sum/400) * 100
print(end= "You percentage of this examination is ")
print(Pmarks,"%")
if Pmarks == 100:
    print("Your grade is A+")
elif Pmarks < 100 and Pmarks > 90:
    print("Your grade is A")
elif Pmarks < 90 and Pmarks > 85:
    print("Your grade is B+")
elif Pmarks < 85 and Pmarks > 80:
    print("Your grade is B")
elif Pmarks < 80:
    print("Your grade is F")
