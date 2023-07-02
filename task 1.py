def check_zero(numberlist):
    count = 0

    for num in numberlist:
        if num == 0:
            count += 1
            if count > 1:
                return False

    return True


array1 = [1, 0, 1, 1]
array2 = [0,1,0,3]

print(check_zero(array1))
print(check_zero(array2))