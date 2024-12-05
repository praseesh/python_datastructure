class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        result = [''] * numRows
        i = 0
        step = 1
        for c in s:
            result[i] += c
            if i == 0:
                step = 1
            elif i == numRows -1:
                step = -1

            i += step
        return "".join(result)
