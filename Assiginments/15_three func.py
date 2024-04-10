def getArray(array, n):
    for i in range(n):
        value = int(input(f"Enter the Value {i+1}:  "))
        array.append(value)
    displayArray(array,n)
    
def displayArray(array,n):
    print("\nThe Entered Array is :\n")
    for i in range(n):
        print(array[i], end=" ")

array = []
n = int(input("Enter the  size of the Array: "))

getArray(array, n)
