n = int(input("Enter the size of the list: "))
print("Enter the values: ")
list1 = []
for i in range(0,n):
    list1.append(int(input()))
duplicates = []
for i in range(0,n-1):
    for j in range(i+1, n):
        if list1[i] == list1[j]:
            duplicates.append(list1[i])


print(f"Duplicates: {duplicates}")