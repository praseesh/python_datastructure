def find_min_diff(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    min_value = float('inf')
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_value:
            min_value = diff
    return min_value

arr = [2, 65, 3, 74, 7, 77, 22, 88]
min_value = find_min_diff(arr)
print(min_value)
    
        