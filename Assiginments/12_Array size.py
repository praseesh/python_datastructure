n = int(input("Enter the size of the array: "))
print("Enter the values of array")
array = []
for i in range(0, n):
    array.append(int(input()))

for i in range(0,n-1):
    for j in range(i+1,n):
        if array[i] < array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
print("Output: ",end=" ")

for i in array:
    print(i, end=", ")
