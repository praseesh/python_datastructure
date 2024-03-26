# Using the ‘switch case’ write a program to accept an input number
# from the user and output the day as follows. 
number = int(input("Enter a number: "))

match number:
    case 1:
        print("It's Sunday")

    case 2:
        print("It's Monday")

    case 3:
        print("It's Tuesday")

    case 4:
        print("It's Wednesday")

    case 5:
        print("It's Thursday")

    case 6:
        print("It's Friday")

    case _:
        print("Enter a valid number")

