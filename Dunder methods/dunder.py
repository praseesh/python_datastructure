str1 = "hello"
str2 = " "
str3 = "world"

# using __str__() method   

new_str = str1.__add__(str2).__add__(str3)
print(new_str)


# using __len__() method    

print(new_str.__len__())