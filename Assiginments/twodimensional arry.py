n = int(input("Enter the size of the array: "))
array = [] 
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Enter the value for element [{i}][{j}]: "))
        row.append(value)
    array.append(row)
    
print("Entered Array: ")
for row in array:
    for value in row:
        print(value, end=" ")
    print()
