class Solution:
    def addBinary(self, a: str, b: str):
        A = int(a, 2)
        B = int(b, 2)
        A = bin(A + B)
        return A[2:]

sol = Solution()
a = "1010"
b = "1011"
s = sol.addBinary(a,b)
print(s)