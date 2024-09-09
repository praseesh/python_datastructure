# import sum_sample 
# print(__name__)
# print(sum_sample.__name__)
# res = sum_sample.sum(10,6)
# print(res) 

# find_sum = sum_sample.sum
# print(find_sum(5,3))

from sum_sample import sum, multi

# s = multi(4,5,6)
# print(s)
s = sum(5,5)
print(s)
f = multi(6,6,6,)
print(f)

def Nmaxelements(list1, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
 
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
 
        list1.remove(max1)
        final_list.append(max1)
 
    print(final_list)
 
 
# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
 
Nmaxelements(list1, N)

