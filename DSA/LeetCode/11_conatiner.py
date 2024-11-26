class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  
print(sol.maxArea([1, 1]))