def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
        print(f"i -> {i}\nstr -> {reversed_string}")
    print(reversed_string)

string = "english"
reverse(string)

s = "praseesh"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

def reverseString(self, s) -> None:
    left = 0
    right =  len(s)-1
    while left < right:
        s[right], s[left] = s[left], s[right]
        left += 1
        right -= 1
    print("Reversed String:", s)
    return s

s = "Programming"
stack = list(s)
rev = ""
while stack:
    rev += stack.pop()
print(rev)
