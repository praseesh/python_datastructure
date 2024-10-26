def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
        print(f"i -> {i}\nstr -> {reversed_string}")
    print(reversed_string)

# First function call
string = "english"
reverse(string)

# Another example of reversing a string
s = "praseesh"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# Using a stack to reverse a string
s = "GeeksforGeeks"
stack = list(s)
rev = ""
while stack:
    rev += stack.pop()
print(rev)
