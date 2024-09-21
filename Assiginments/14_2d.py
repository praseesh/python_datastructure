n = int(input("Enter the size of arrays : "))
array = []
for i in range(n):
    rows =[]
    for j in range(n):
        value = int(input(f"Enter the Array Values [{i}][{j}]: "))
        rows.append(value)
    array.append(rows)
print("First Array Completed...!!! ")


array2 = []
for i in range(n):
    row =[] 
    for j in range(n):
        values = int(input(f"Enter the values of Second Array [{i}] [{j}] :"))    
        row.append(values)
    array2.append(row)

sum = []
for i in range(n):
    row2 = []
    for j in range(n):
        values = array[i][j] + array2[i][j]
        row2.append(values)
    sum.append(row2)
     
print("Sum of 2 arrays is: ")
for i in sum:
    for j in i:
        print(j, end=" ")
    print()
    
