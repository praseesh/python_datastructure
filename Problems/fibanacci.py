t1 = 0
t2 = 1
nt = t1 +t2

n =int(input("Enter the Number: "))
print(t1, t2,end=" ")
for i in range(2,n+1):
    print(nt, end=" ")
    t1 = t2
    t2 = nt
    nt = t1 + t2
    