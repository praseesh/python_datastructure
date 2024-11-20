def prime_number_or_not(n):
    if n <= 1:
        print(f"Entered Number {n} is not a prime")
        return
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(f"Entered Number {n} is Prime")
    else:
        print(f"Entered Number {n} is not a prime")
    
n = int(input("Enter a number to check Prime Number or Not: "))
prime_number_or_not(n)