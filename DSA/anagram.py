class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            dict2[t[i]] = dict2.get(t[i], 0) + 1
        for i in dict1:
            if dict1[i] != dict2.get(i):
                return False
        return True

cls = Solution()
s = "hello"
t = "hello"
result = cls.isAnagram(s, t)
if result:
    print("The given strings are anagrams: True")
else:
    print("The given strings are anagrams: False")