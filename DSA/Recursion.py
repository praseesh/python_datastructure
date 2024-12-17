def recursion(n):
    if n <= 1:
        return 1
    recursion(n-1)
    print(n, end=" ")
    recursion(n-1)

recursion(5)