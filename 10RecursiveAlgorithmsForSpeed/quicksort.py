def partition(arr, start, end):
    idx = start - 1
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] <= pivot:
            idx += 1
            arr[j], arr[idx] = arr[idx], arr[j]
    arr[end], arr[idx + 1] = arr[idx + 1], arr[end]
    return idx + 1

def quicksort(arr, start, end):
    if start < end:
        piv_idx = partition(arr, start, end)
        quicksort(arr, start, piv_idx - 1)
        quicksort(arr, piv_idx + 1, end)

arr = [0, 1, 2, 3, 6, 5]
quicksort(arr, 0, len(arr) - 1)

for val in arr:
    print(val, end=" ")
print()
