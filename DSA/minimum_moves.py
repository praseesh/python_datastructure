# minimum_moves

def minMoves2(nums):
    nums.sort()
    a = nums[len(nums)//2]
    print(nums)
    count = 0
    for i in range(len(nums)):
        count += abs(nums[i] - a)
    return count

nums = [1,10,2,9]
minMoves2(nums)