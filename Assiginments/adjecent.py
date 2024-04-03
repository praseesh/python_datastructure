n = int(input("Enter the size: "))
list1 = []
for i in range(0,n):
    e = int(input(f"Enter the values {i+1}: "))
    list1.append(e)

print(list1)
a = []
for i in range(n-1):
    a.append(list1[i] * list1[i+1])
    

print(a)