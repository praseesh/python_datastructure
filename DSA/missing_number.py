class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        missing_number = expected_sum - actual_sum
        print("Missing Number: ", missing_number)
        return missing_number

sol = Solution()
sol.missingNumber([0,1,2,4])