def find_second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        if num < largest and num > second_largest:
            second_largest = num
    return second_largest
 
arr = [2, 65, 3, 74, 7, 77, 22, 88]       
print(find_second_largest(arr))