def binary_search_iterative(arr, target):
    start = 0
    end = len(arr)-1
    
    while start <= end:
        middle = start + (end - start)//2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            end = middle - 1
        elif arr[middle] < target:
            start = middle +1
            
    return -1

arr = [1,2,3,4,5,6,7,8]
print(binary_search_iterative(arr,8))

