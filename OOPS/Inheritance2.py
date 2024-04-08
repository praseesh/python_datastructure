class BaseClass:
    def __init__(self):
        print("This is Base init")
        
    def set_name(self,name,place, city):
        print("This is Base Set name")
        self.name = name
        self.place = place
        self.city = city
        
class SubClass(BaseClass):
    def __init__(self):
    
        print("This is Sub init")
        
    def set_name(self,name,place, city):
        super().set_name(name,place,city)
        print("This is Sub Set name")  
        
        
    def display(self):
        print(f"Name: {self.name}\nPlace: {self.place}")
        
# person1 = BaseClass()
person1 = SubClass()
person1.set_name("Jacob", "Berlin", "Delta")
person1.display()
