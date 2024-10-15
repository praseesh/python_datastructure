def climbing_stairs(n):
    if n == 1:
        return 1
    current = 1
    previous = 1
    for i in range(2, n+1):
        temp = current 
        current = previous + current
        previous = temp
    return current

