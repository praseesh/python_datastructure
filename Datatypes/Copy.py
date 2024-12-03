import copy
list1 = [1,2,[3,4],5]

list2 = copy.copy(list1)
list2[2][0] = "B"
print(list1)
print(list2)

list3 = copy.deepcopy(list1)
list3[1][1] = "a"
print(list1)
print(list2)
print(list3)