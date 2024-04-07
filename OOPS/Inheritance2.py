class BaseClass:
    def __init__(self, name, place, city):
        self.name = name
        self.place = place
        self.city = city
        print("This is Base init")
        
    def set_name(self,name):
        self.name = name
        
class SubClass(BaseClass):
    
    def display(self):
        print(f"Name: {self.name}\nPlace: {self.place}")
        
person1 = SubClass("Jacob", "Berlin", "Tokyo")
person1.display()
