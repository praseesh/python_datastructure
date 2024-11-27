def sum_pairs(arr,target):
    n = len(arr)
    found = False
    for num in range(n-1):
        print(num)
        for nums in range(n+1, n):
            if arr[num] + arr[nums] == target:
                print(f"{arr[num]}, {arr[nums]}")
                found = True
    if not found:
        print("No Pairs Found..!!!")
arr = [2,6,7,9,4]  
target = 16
sum_pairs(arr, target)
    