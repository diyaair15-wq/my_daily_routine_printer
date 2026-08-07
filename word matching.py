def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) >= 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    return ctr

count = match_words(['abc', 'dlm', 'lpw', 'dpl', '1011'])
print("number of words having first and last character same is:", count)