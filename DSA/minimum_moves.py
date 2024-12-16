# minimum_moves

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[len(nums)//2]
        print(nums)
        count = 0
        for i in range(len(nums)):
            count += abs(nums[i] - a)
        return count