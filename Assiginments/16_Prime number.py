num = int(input("Enter a number to check Prime number or not: "))
if num ==0 or num ==1: 
    print(f"{num} is Not a Prime Number")

else:
    flag = 0
    for i in range(2,num):
        if num % i==0:
            flag = 1
    if flag ==1:
        print(f"{num} is Not a Prime Number")

    else:
        print(f"{num} is a Prime Number")


        

