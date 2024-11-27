def first_non_repeating_character(word):
    occurrence = {}
    for letter in word:
        if letter in occurrence:
            occurrence[letter] += 1
        else:
            occurrence[letter] =1
    print(occurrence)
    for letter in word:
        if occurrence[letter] == 1:
            print(occurrence)
            return letter
    
    return "No Non-repeating letter Found"
word = "swiss"
result = first_non_repeating_character(word)
print(result)
        