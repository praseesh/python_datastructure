<<<<<<< HEAD
def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i+reversed_string
        print(f"i-> {i}\nstr-> {reversed_string}")
    print(reversed_string)
    
string = "english"

reverse(string)
=======
s = "praseesh"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


s = "GeeksforGeeks"
stack = list(s)
rev = ""
while stack:
    rev += stack.pop()
print(rev)
>>>>>>> 9a3e4168ea3d0ad9760e519f75e71c39191e3fb5
