numbers = [4, 2, 7, 1, 3]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1
    numbers[j + 1] = key

print("Sorted list:", numbers)
