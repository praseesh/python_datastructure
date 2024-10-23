s = "praseesh"

rev = ""

for ch in s:
  
 
    rev = ch + rev

print(rev)


s = "GeeksforGeeks"

# Convert the string into a list to use it as a stack
stack = list(s)

# Initialize an empty string to hold the reversed result
rev = ""

# Continue looping until the stack is empty
while stack:
  
    # Remove the top element from the stack 
    # and add it to the reversed string
    rev += stack.pop()

print(rev)
