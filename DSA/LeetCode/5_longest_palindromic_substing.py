def longest_palindromic_substring(s):
    def check_palindrome(left,right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            return s[left+1:right]
        
    longest = ""
    for i in range(len(s)):
        pass