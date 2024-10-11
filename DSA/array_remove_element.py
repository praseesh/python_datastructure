class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        print("After Removal: ",i)
        return i
    
sol = Solution()
arr = [3,2,2,3,5,7,5,2,3]
value = 3
sol.removeElement(arr,value)