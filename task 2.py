def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = [5, 2, 8, 1, 3]

bubble_sort(array)
print("sortedlist :",array)
