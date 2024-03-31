word = input("Enter a word to check Palindrome or not: ")
flag =0
n = len(word)

for i in range(0, n//2):
    if word[i] != word[n-i-1]:
        flag = 1
        break

if flag == 0:
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is not a Palindrome")
