def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr+=1
            lst.append(word)
    print("List of letters with first and last letters same are \n", lst)
    return ctr

count = match_words(['abc', 'bsc', 'aba', '1212231', '1221'])
print("The number of words having first and last letter same are: ", count)