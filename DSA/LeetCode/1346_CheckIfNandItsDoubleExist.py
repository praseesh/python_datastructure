def check_if_exist(arr):
    values = set(arr)
    for num in arr:
        if num*2 in values and num * 2 != num:
            return True
        if num == 0 and arr.count(0) > 1:
            return True
    return False
    
arr = [10,2,5,3]
print(check_if_exist(arr))