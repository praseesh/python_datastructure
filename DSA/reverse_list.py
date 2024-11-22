def reverse_list(arr):
    size = len(arr)
    i = 0
    while i < size // 2:
        arr[i], arr[size - 1 - i] = arr[size - 1 - i], arr[i]
        i += 1
    return arr
        
arr = [1,2,3,4,5,6]
reversed = reverse_list(arr)
print(reversed)