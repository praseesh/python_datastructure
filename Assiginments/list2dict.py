list1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
a = {}
for i in list1:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
b = sorted(a.items())
for i,j in b:
    print(f"{i}: {j}")
