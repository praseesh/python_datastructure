"""                        Move items to right                       """

arr = [6,1,6,8,10,4,15,6,3,4,6]

def move(a):
    num = int(input("Enter a Number to move Right:   "))
    for i in range(0,len(arr)):
        if arr[i] == num:
            arr.append(arr[i])
            arr.pop(i)
    print(arr)
    
move(arr)


"""                          Time complexity: O(n)                     """
"""                          Space Complexity: O(1)                    """