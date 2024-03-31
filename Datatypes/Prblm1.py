list1 = ['a', 'b', 'c', 'd', 'a']

output = {}
for i in list1:
    if i in output:
        output[i] = output[i] + 1

    else:
        output[i] = 1

print(output)