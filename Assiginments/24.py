class Area:
    def circle(radius):
        pi = 3.14
        return pi * radius ** 2
    
    def rectangle(width,height):
        return width * height
    
    def triangle(base, height):
        return (base * height) / 2
    
    def square(side):
        return side ** 2

class MyClass(Area):
    def main():
        try:
            choice=int(input("1. for circle\n2. for square\n3. for rectangle\n4. for triangle\n"))
        except Exception as e:
            print("An error occur...",e)
        try:
            if choice == 1:
                    radius = float(input("Enter the Radius of the Circle: "))
                    print("Area of Circle:", Area.circle(radius))
            if  choice == 2:
                    side = float(input("Enter the Side of the Square: "))
                    area = Area.square(side)  
                    print("Area of the square is: ", area)              
            if  choice == 3:
                    length = float(input("Enter the length of the Rectangle: "))
                    width = float(input("Enter the Width of the Rectangle: "))
                    area = Area.rectangle(length,width)
                    print("Area of the Rectangle is: ", area)              
                    
            if  choice == 4:
                    base = float(input("Enter the length of the Triangle: "))
                    height = float(input("Enter the Width of the Triangle: "))
                    print(f"Area of the Rectangle is: {Area.rectangle(base, height)}")
        except Exception as e:
                print(f"An error occur...{e}")
        
MyClass.main()
            