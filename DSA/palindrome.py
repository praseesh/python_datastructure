def palindrome(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            print("Not a Palindrome")
            return False
    print("Its a Palindrome")
    return True

word = "malayala"
palindrome(word)