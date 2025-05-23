def has_duplicate_value(array):
    existing_values = {}

    for item in array:
        if item in existing_values:
            return True
        else:
            existing_values[item] = True  

    return False

numbers = ["apple", "banana", "grape", "apple"]
print("Has duplicates?", has_duplicate_value(numbers))  
