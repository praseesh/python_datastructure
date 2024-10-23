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
