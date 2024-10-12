class Solution:
    def replaceElements(self, arr) :
        greatest = -1  
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]  
            arr[i] = greatest  
            greatest = max(greatest, current)  
        
        return arr
    def replace(self, arr):
        n = len(arr)
        max_from_right = -1
        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = max_from_right
            max_from_right = max(max_from_right, current)

        return arr
sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]))
print(sol.replace([17,18,5,4,6,1]))
