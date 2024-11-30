class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst, s = lst[::-1], ""
        for i in lst:
            s += i
            s += ' '
        return s.strip()