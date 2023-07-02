word = "Minite"

vowels = 'aeiou'
vowel_count = 0

for char in word.lower():
    if char in vowels:
        vowel_count += 1
        if vowel_count >= 3:
            print("False")
            break
else:
    print("True")