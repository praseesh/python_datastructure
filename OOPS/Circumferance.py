class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        circum = 2 * self.pi * self.radius
        return circum
        
cir1 = Circle(4)
cir1 = cir1.circumference() 
print(cir1)