class SortableArray:
    def __init__(self, array):
        self.array = array

    def swap(self, pointer_1, pointer_2):
        temp_value = self.array[pointer_1]
        self.array[pointer_1] = self.array[pointer_2]
        self.array[pointer_2] = temp_value

    def partition(self, left_pointer, right_pointer):
        pivot_position = right_pointer
        pivot = self.array[pivot_position]
        right_pointer -= 1

        while True:
            while left_pointer < len(self.array) and self.array[left_pointer] < pivot:
                left_pointer += 1
            while right_pointer >= 0 and self.array[right_pointer] > pivot:
                right_pointer -= 1
            if left_pointer >= right_pointer:
                break
            else:
                self.swap(left_pointer, right_pointer)

        self.swap(left_pointer, pivot_position)
        return left_pointer

arr = SortableArray([0,5,2,1,6,3])
pivot_index = arr.partition(0, len(arr.array) - 1)
print(arr.array)
print("Pivot index:", pivot_index)
