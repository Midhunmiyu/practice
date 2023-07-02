def unique(word):
    a = len(word)
    b =len(set(word))
    if a == b:
        return True

    return False

word = "calculator"
word1 = "mobile"
print(unique(word))
print(unique(word1))
