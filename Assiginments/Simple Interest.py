amount = int (input("Enter the Principal Amount: "))
interest = float(input("Enter Interest Rate: "))
year = float(input("Select Tenure: "))

si = (amount*interest*year)/100

print("Simple interest is: "+str(si))