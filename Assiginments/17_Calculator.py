class MathOperations:
    def addition(self,a,b):
        sum = a + b
        return sum
    
    def subtraction(self,a,b):
        sum = a - b
        return sum
    
    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Can't divided by Zero...!"
    
    def multiply(self,a, b ):
        sum = a * b
        return sum
        
a = int(input("Enter First number: "))   
b = int(input("Enter Second number: "))        
operator = input("Select Operator: \n\n1. for addition\n2. for subtraction\n3. for multiplication\n4. for division\n\nPlease enter valid input:   ")

num = MathOperations()

if operator == "1":
    result = num.addition(a,b)
    print(f"Answer is: {result}")
    
elif operator == "2":
    result = num.subtraction(a,b)
    print(f"Answer is: {result}")
    
elif operator == "3":
    result = num.multiply(a,b)
    print(f"Answer is: {result}")
    
elif operator == "4":
    try:
        result = num.division(a,b)
        print(f"Answer is: {result}")
    except ZeroDivisionError:
        print("can't divided by Zero")
          
else:
    print("wrong command")



        