# Write a program to find the sum of all the odd numbers for a given limit


limit = int(input("Enter a limit: "))
sum = 0 
for i in range(1,limit+1,2):
    sum = sum + i

print(f"Sum of odd numbers: {sum}")