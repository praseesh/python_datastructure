def tax_calculate(i):
    tax = 0
    if i <= 250000:
        tax = 0
    elif i <=500000:
        tax = i*0.05
    elif i <= 1000000:
        tax = i*0.20
    elif i<=5000000:
        tax = i*0.30
    else:
        print("Out of Range")
    return tax
ai = int(input("Enter Your Annual Income: "))
tax = tax_calculate(ai)
print(f"Your annual Tax is : {tax}")