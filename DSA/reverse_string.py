class Solution:
    def reverseString(self, s) -> None:
        left = 0
        right =  len(s)-1
        while left < right:
            s[right], s[left] = s[left], s[right]

            left += 1
            right -= 1
        print("Reversed String:", s)
        return s
    
sol = Solution()
sol.reverseString(["H","a","n","n","a","h"])
