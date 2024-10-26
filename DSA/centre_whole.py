def center_whole(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or j==n-1 or i==n-1:
                print("* ",end="")
            else:
                print("  ",end="")
        print("\n")


def full_pyramid(n):
    for i in range(0,n+1):
        for j in range(0,i):
            print("* ",end="")
        print("\n")
            
full_pyramid(n=5)