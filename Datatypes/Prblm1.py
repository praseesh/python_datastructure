list1 = ['a', 'b', 'c', 'd', 'a']

output = {}
for i in list1:
    if i not in output:
        output[i] = 1
    else:
        output[i] += 1 
print(output)