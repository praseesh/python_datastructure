marks = []
subjects = ["English", "Hindi", "Physics", "Chemistry", "Biology", "Maths"]
name = input("Enter Your Name: ")
sum = 0
for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))
    sum +=mark
    marks.append(mark)

average = sum/6
    
print(average)
for i in marks:
    if  average <= 100 and  average >= 90:
        print(f"{name} your grade is A")
        break

    elif  average <= 89 and  average >= 80:
        print(f"{name} your grade is B")
        break

    elif  average <= 79 and  average >= 70:
        print(f"{name} your grade is C")
        break
        
    elif  average <= 69 and  average >= 60:
        print(f"{name} your grade is D")
        break

    elif  average <= 59 and  average >= 50:
        print(f"{name} your grade is D")
        break
    
    elif average < 50 and average > 0:
        print(f"{name} You Failed")
        break
    
    else:
        print("Entered Mark is out of range")
        break



