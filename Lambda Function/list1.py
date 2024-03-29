list1 = [12,57,4,3,23,6,32,325,24,35,1,45,34,54,342,44]

def even(a):
    if a % 2 == 0:
        return a
    
f = filter(even,list1)
print(list(f))