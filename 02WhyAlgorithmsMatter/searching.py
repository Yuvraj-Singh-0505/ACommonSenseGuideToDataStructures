def linear_search(array, value):
    for element in array:
        if element == value:
            return value
        elif element > value:
            break
    return None

numbers = [3, 17, 75, 80, 202]
result = linear_search(numbers, 22)

if result is None:
    print("Value not found")
else:
    print("Value found:", result)
