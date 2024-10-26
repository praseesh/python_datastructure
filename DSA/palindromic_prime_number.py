def palindromic_prime(num):
    reversed_num = int(str(num)[::-1])
    if num == reversed_num:
        if num > 1:
            for i in range(2,num):
                if (num%2) == 0:
                    print(f"{num} is not a palindromic number")
                    break
            else:
                print(num, "is a Prime")
        
def reverse(num):
    for i in range(int(len(num)/2)):
        if num[i] != num[len(num)-i-1]:
            return False
    return True

num = 6
palindromic_prime(num)