word = input("Enter a random word: ")
char = input("Which character do you choose from the given word: ")
count = 0
for i in range(len(word)):
    if word[i] == char:
        count += 1

print("The letter", char, "is repeated", count, "time(s)")
