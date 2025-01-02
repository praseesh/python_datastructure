class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = int(a, 2)
        B = int(b, 2)
        
        A = bin(A + B)
        return A[2:]