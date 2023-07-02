a =[1,2,4,32,12,6,8]
b = [2,6,10,12,14,17]

new = []

for number in a:
    if number not in b:
        new.append(number)

print("Numbers present in array a but not in b:", new)