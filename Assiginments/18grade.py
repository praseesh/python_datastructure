def grade(x,y,z):
    a = x * 0.7
    b = y * 0.2   
    c = z * 0.1

    result = a + b + c
    return result

a =float(input("Enter the Marks in Written Test:  "))
b =float(input("Enter the Marks in Lab Tests:  "))
c =float(input("Enter the Marks in Assignments:  "))

Grade = grade(a,b,c)

print(f"Student Grade is:  {Grade:.2f}")
