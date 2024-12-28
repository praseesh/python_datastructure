class Solution:
    def decrypt(self, code, k):
        n = len(code)
        for i in range(n):
            if k == 0:
                return [0] * n
            result = [0] * n
        for i in range(n):
            if k > 0:
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            elif k < 0:
                result[i] = sum(code[(i - j) % n] for j in range(1, abs(k) + 1))
        return result
sol = Solution()
code = [5,7,1,4]

k = 3
sol.decrypt(code,k)