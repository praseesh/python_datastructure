def divisible(n):
    if n % 10 == 0:
        return True
    else:
        return False
    
a = int(input("Enter a number to check divisible by 10: "))

if divisible(a):
    print(f"TRUE")

else:
    print(f"FALSE")