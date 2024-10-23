s = "praseesh"

rev = ""

for ch in s:
  
 
    rev = ch + rev

print(rev)


s = "GeeksforGeeks"

stack = list(s)

# Initialize an empty string to hold the reversed result
rev = ""

# Continue looping until the stack is empty
while stack:
  
    # Remove the top element from the stack 
    # and add it to the reversed string
    rev += stack.pop()

print(rev)
