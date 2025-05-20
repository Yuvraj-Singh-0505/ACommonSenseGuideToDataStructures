def binary_search(array, value):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        if guess == value:
            return mid  
        elif guess < value:
            low = mid + 1
        else:
            high = mid - 1

    return None  

numbers = [3, 17, 22, 75, 80, 202]
result = binary_search(numbers, 22)

if result is not None:
    print("Value found at index:", result)
else:
    print("Value not found")
