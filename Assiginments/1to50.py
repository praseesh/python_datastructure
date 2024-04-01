for i in range(1,51):
    if i % 3 == 0 or i % 5 ==0:
        if i % 3 == 0 and i % 5 ==0:
             print("Hi Hello")
        elif i % 3 == 0:
            print("Hello")
        elif i % 5 ==0:
                print("Hi") 
    else:
        print(i)