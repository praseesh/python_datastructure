def longest_palindromic_substring(s):
    def check_palindrome(left,right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        p1 = check_palindrome(i,i)
        p2 = check_palindrome(i,i+1)
        
        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2
    return longest

s = "ababd"
print(longest_palindromic_substring(s))