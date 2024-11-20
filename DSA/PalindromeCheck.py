def is_palindrome(s):
    reversed_string = []
    for i in range(len(s)-1,-1,-1):
        reversed_string.append(s[i])
    reversed_string = ''.join(reversed_string)
    if reversed_string == s:
        print("Given String is Palindrome")
    else:
        print(f"{s} is Not a Palindrome")

s = "malayalam"    
is_palindrome(s)