numbers = [3, 17, 80, 202]
new_value = 75
index = 0
while index < len(numbers) and numbers[index] < new_value:
    index += 1
numbers.insert(index, new_value)
print("Ordered array:", numbers)
