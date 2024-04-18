name = ["shazil","praseesh","althaf"]
values = [2,4,1]

for i in range(len(values)-1):
    for j in range(i+1,len(values)):
        if values[i]<values[j]:
            temp = values[i]
            values[i] = values[j]
            values[j] = temp
print(values)
dict1 = {}
for i in range(len(name)):
    dict1[name[i]] = values[i]
    
print(f"Sorted List: {dict1}")

