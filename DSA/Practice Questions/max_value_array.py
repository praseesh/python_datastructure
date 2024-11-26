def maximum_number(arr):
    max1 = float('-inf')
    max2 = float('-inf')
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num 
            print(f"max: {max1},max: {max2}")
        if num > max2 and num < max1:
            max2 = num
    print(f"max: {max1},max: {max2}")
    max_value = max1 + max2
    return max_value      
        

arr = [2, 65, 3, 74, 7, 77, 22, 88]       
print(maximum_number(arr))