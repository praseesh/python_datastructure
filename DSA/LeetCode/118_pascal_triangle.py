class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        triangle = [[1]]
        for i in range(1,numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
    
sol = Solution()
print(sol.generate(5))