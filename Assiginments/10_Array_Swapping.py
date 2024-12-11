n = int(input("Enter the size of arrays: "))
array1 = []
array2 = []
print("Enter the values of Array 1")
for i in range(0,n):
    array1.append(int(input()))
print("Enter the values of Array 2")
for i in range(0,n):
    array2.append(int(input()))
for i in range(0,n):
    temp1 = array1[i]
    temp2 = array2[i]
    array1[i] = temp2
    array2[i] = temp1
print("Array1: ",end="")
for i in array1:
    print (i,end=",")
print()
print("Array2: ",end="")
for i in array2:
    print (i,end=",")