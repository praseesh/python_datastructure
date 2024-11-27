def string_occurrence(word):
    occurrence = {}
    for letter in word:
        if letter in occurrence:
            occurrence[letter] += 1
        else:
            occurrence[letter] = 1
    return occurrence
word = "hello"
result = string_occurrence(word)
print(result)
