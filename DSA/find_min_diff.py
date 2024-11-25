def find_min_diff(arr):
    n = len(arr)
    sorted_array =[]
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)
    return arr
arr = [2,65,3,74,7,77,22,88]
find_min_diff(arr)
    
        