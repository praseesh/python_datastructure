import re

pattern = r'10*'
print(re.search(pattern,"5108910008"))

# check for the pattern dd-mm-yyyy

# pattern = r'\d{1,2}-\d{1,2}-\d{2,4}'
# print(re.search(pattern,"44-55-3232"))
 
# find the word with exactly 8 words

# pattern = r'\w{8}'
# print(re.search(pattern,"this is abstract"))