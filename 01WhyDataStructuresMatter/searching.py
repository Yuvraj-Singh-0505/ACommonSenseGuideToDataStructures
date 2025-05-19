fruits = ["apples", "bananas", "cherries", "dates", "elderberries"]

search_item = "dates"

for i in range(len(fruits)):
    if fruits[i] == search_item:
        print("Found at index", i)
        break
