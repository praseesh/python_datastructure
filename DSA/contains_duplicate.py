class Solution:
    def containsDuplicate(self, nums) -> bool:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))