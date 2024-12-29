class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = 0

        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i
                break

        if pivot == 0:
            nums.sort()
            return

        swap = n - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1

        nums[pivot - 1], nums[swap] = nums[swap], nums[pivot - 1]

        nums[pivot:] = sorted(nums[pivot:])