def pattern(n):
    for i in range(n):
        for j in range(i,n):
            print('*', end=" ")
        print('')
        
pattern(5)