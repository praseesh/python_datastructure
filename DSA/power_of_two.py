class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n %  2 != 0:
                return False
            n //= 2
        return n == 1
    
sol = Solution()
print(sol.isPowerOfTwo(443))
print(sol.isPowerOfTwo(522))
print(sol.isPowerOfTwo(512))
