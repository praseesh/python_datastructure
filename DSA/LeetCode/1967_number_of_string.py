def numOfStrings(patterns, word):
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count

# Test cases
print(numOfStrings(["a","abc","bc","d"], "abc"))  
print(numOfStrings(["a","b","c"], "abb"))  
print(numOfStrings(["a","a","a"], "ab"))            