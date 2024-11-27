def sum_pairs(arr, target):
    seen = set()
    found = False
    for num in arr:
        complement = target - num
        if complement in seen:
            print(f"{complement}, {num}")
            found = True
        seen.add(num)
    if not found:
        print("No pairs found.")
        
arr = [2,6,7,9,4]  
target = 16
sum_pairs(arr, target)