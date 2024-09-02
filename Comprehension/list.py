list1 = []
list1 = [input() for i in range(5)]
print(list1)


list2 = []
for i in range(5):
    n = int(input(f"Enter numbers {i+1}: "))
    list2.append(n)
print (list2)