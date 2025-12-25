name = "Manitt"
age = 12
is_student = True
weight = 41.24

print("Name:",name)
print("the data type of the following value is", type (name))

print("Age:",age)
print("the data type of the following value is", type(age))

print(name,",is he a student?", is_student)
print("the data type of the following value is", type(is_student))

print("Weight of the following person is:",weight)
print("the data type of the following value is", type(weight))

print("\n after typecasting", name, "found out that he could simply change the data type of the value, in the end it just got him thes results")
age = float(age)
print(age)
print("This was rather interesting as", name," found that his age could be changed to another data type and be shown like this:", type(age))
weight = int(weight)
print(weight)
print("This was rather interesting as", name," found that his weight could be changed to another data type and be shown like this:", type(weight))

