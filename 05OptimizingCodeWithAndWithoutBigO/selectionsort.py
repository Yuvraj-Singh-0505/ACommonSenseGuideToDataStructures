numbers = [4, 2, 7, 1, 3]
for i in range(len(numbers)):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    temp = numbers[i]
    numbers[i] = numbers[min_index]
    numbers[min_index] = temp

print("Sorted list:", numbers)
