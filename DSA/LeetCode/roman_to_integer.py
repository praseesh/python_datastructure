class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        sum_ = 0
        a = 0
        for c in range(len(s)-1, -1, -1):
            
            if d[s[c]] >= a:
                sum_ += d[s[c]]
            else:
                sum_ -= d[s[c]]
            a = d[s[c]]            
            
        return sum_
