def get_array():
    n = int(input("Enter the size of arrays : "))
    array = []
    for i in range(n):
        rows =[]
    for j in range(n):
        value = int(input(f"Enter the Array Values [{i}][{j}]: "))
        rows.append(value)
    array.append(rows)     