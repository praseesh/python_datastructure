def twoSum(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

nums1 = [2, 7, 11, 15]
target1 = 13
print(twoSum(nums1, target1)) 

