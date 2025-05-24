arr = [4, 2, 7, 1, 3]
n = len(arr)
step = 1  

print("Original array:", arr)

for i in range(n):
    swapped = False
    print(f"\nPassthrough #{i+1}:")

    for j in range(n - 1 - i):
        print(f"Step #{step}: Compare {arr[j]} and {arr[j+1]}")
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"Step #{step+1}: Swap -> {arr}")
            swapped = True
            step += 1  
        else:
            print(f"Step #{step+1}: No swap -> {arr}")
            step += 1
        step += 1

    if not swapped:
        print("No swaps made in this pass3 — array is sorted.")
        break

print("\nSorted array:", arr)
