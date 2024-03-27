n = int(input("Enter the Size: "))
arr = []
count = 0
for i in range(n):
    num = (int(input(f"Enter element {i+1}: ")))
    arr.append(num)
    if num%2==1:
        count +=1

print("Input:", arr)
print(f"Number of even numbers in the given array is: {count}")